from django.core.paginator import Paginator
from django.shortcuts import render
import pandas as pd
import pickle
from . import data_process as dp

def load_model():
    with open('./static/models/final.pickle', 'rb') as file:
        churn_model, features = pickle.load(file)
    return churn_model, features


def preprocess_data(raw_data:pd.DataFrame):
    raw_data["low_q1_total"] = raw_data['totalcharges'] <= 138.6875
    raw_data["low_q3_tenure"] = raw_data['tenure'] <= 30.0
    raw_data['partner+dependents_no'] = int((raw_data['partner'] == 'No') & (raw_data['dependents'] == 'No'))
    raw_data['total_charges_binary_1500'] = int((raw_data['totalcharges'] < 1500))

    
    raw_data = dp.create_contract_end_soon_feature(raw_data)
    raw_data['billing_ratio'] = (
        raw_data['totalcharges'] / (raw_data['monthlycharges'] * raw_data['tenure'])
        if raw_data['monthlycharges'] > 0 and raw_data['tenure'] > 0 else 0    )

    raw_data['monthly_charges_category'] = dp.categorize_monthly_charges(raw_data['monthlycharges'])
    raw_data['tenure_category'] = dp.categorize_tenure(raw_data['tenure'])
    raw_data = dp.to_binary(raw_data)
    raw_data = dp.do_1hot(raw_data)
def customer_list(request):
    # CSV 파일을 Pandas로 불러오기
    
    origin_df = pd.read_csv("./static/database/origin.csv")
    modeals_df = pd.read_csv("./static/database/model.csv")

    # 필요한 컬럼만 선택 (고객 ID, 성별, 월 요금, 가입 기간)
    origin_df = origin_df[['customerID', 'gender', 'MonthlyCharges', 'tenure']]

    # LightGBM 모델로 예측 진행
    model, ml_features = load_model()
    
    # 예측을 위한 feature 선택
    ml_features = ['gender', 'seniorcitizen', 'partner', 'dependents', 'tenure', 'phoneservice', 'paperlessbilling', 'monthlycharges', 'totalcharges', 'low_q1_total', 'low_q3_tenure', 'total_charges_binary_1500', 'contract_end_soon', 'billing_ratio', 'multiplelines_No', 'multiplelines_No phone service', 'multiplelines_Yes', 'internetservice_DSL', 'internetservice_Fiber optic', 'internetservice_No', 'onlinesecurity_No', 'onlinesecurity_Yes', 'onlinebackup_No', 'onlinebackup_Yes', 'deviceprotection_No', 'deviceprotection_Yes', 'techsupport_No', 'techsupport_Yes', 'streamingtv_No', 'streamingtv_Yes', 'streamingmovies_No', 'streamingmovies_Yes', 'contract_Month-to-month', 'contract_One year', 'contract_Two year', 'paymentmethod_Bank transfer (automatic)', 'paymentmethod_Credit card (automatic)', 'paymentmethod_Electronic check', 'paymentmethod_Mailed check', 'monthly_charges_category_High', 'monthly_charges_category_Low', 'monthly_charges_category_Medium', 'tenure_category_Long-term', 'tenure_category_Medium-term', 'tenure_category_Short-term']
    features = modeals_df[ml_features]

    # 모델 예측 (예측 확률을 사용해 위험도 계산)
    predictions = model.predict_proba(features)[:, 1]

    # 위험도를 예측 확률 기반으로 분류 (저위험, 중위험, 고위험)
    origin_df['RiskCategory'] = pd.cut(predictions, bins=[0, 0.4, 0.7, 1], labels=["저위험", "중위험", "고위험"])

    # 필터 값 가져오기
    search_query = request.GET.get('search', '').strip().upper()
    gender_filter = request.GET.get('gender', '')
    risk_filter = request.GET.get('risk', '')

    # 필터 적용 (ID 검색, 성별 필터, 위험군 필터)
    if search_query:
        origin_df = origin_df[origin_df['customerID'].str.upper().str.contains(search_query)]

    if gender_filter:
        origin_df = origin_df[origin_df['gender'] == gender_filter]

    if risk_filter:
        origin_df = origin_df[origin_df['RiskCategory'] == risk_filter]

    # 결과를 최대 100개로 제한
    origin_df = origin_df.head(200)

    # 페이지네이션을 위한 Paginator 클래스 사용
    paginator = Paginator(origin_df.to_dict('records'), 10)  # 페이지당 10개의 고객을 표시

    # 요청한 페이지 번호 가져오기
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'customer/customer_list.html', {'page_obj': page_obj})

# 고객 정보 입력 페이지 및 예측 처리
def predict_churn(request):
    result = None  # 초기 상태는 결과 없음
    if request.method == 'POST':
        # 입력된 데이터를 받음
        gender = request.POST.get('gender')
        seniorcitizen = request.POST.get('seniorcitizen')
        if seniorcitizen == 'yes':
            seniorcitizen = True
        elif seniorcitizen == 'no':
            seniorcitizen = False
        partner = request.POST.get('partner')
        dependents = request.POST.get('dependents')
        phoneservice = request.POST.get('phoneservice')
        multiplelines = request.POST.get('multiplelines')
        internetservice = request.POST.get('internetservice')
        onlinesecurity = request.POST.get('onlinesecurity')
        onlinebackup = request.POST.get('onlinebackup') 
        deviceprotection = request.POST.get('deviceprotection') 
        techsupport = request.POST.get('techsupport')
        streamingtv = request.POST.get('streamingtv') 
        streamingmovies = request.POST.get('streamingmovies') 
        contract = request.POST.get('contract') 
        paperlessbilling = request.POST.get('paperlessbilling')
        paymentmethod = request.POST.get('paymentmethod')

        # 월 요금과 가입 기간 기본값 설정 (값이 없을 때 최빈값 사용)
        monthlycharges = request.POST.get('monthlycharges')
        tenure = request.POST.get('tenure')

        # 기본값 설정 (monthlycharges: 20.05, tenure: 1)
        if not monthlycharges:
            monthlycharges = 20.05  # 기본값 (최빈값)
        else:
            monthlycharges = float(monthlycharges)

        if not tenure:
            tenure = 1  # 기본값 (최빈값)
        else:
            tenure = int(tenure)

        # TotalCharges 계산
        totalcharges = tenure * monthlycharges

        result = {
            'gender': [gender],
            'seniorcitizen': [seniorcitizen],
            'partner': [partner],
            'dependents': [dependents],
            'tenure': [tenure],
            'phoneservice': [phoneservice],
            'multiplelines': [multiplelines],
            'internetservice': [internetservice],
            'onlinesecurity': [onlinesecurity],
            'onlinebackup': [onlinebackup],
            'deviceprotection': [deviceprotection],
            'techsupport': [techsupport],
            'streamingtv': [streamingtv],
            'streamingmovies': [streamingmovies],
            'contract': [contract],
            'paperlessbilling': [paperlessbilling],
            'paymentmethod': [paymentmethod],
            'monthlycharges': [monthlycharges],
            'totalcharges': [totalcharges]
        }

      

    return render(request, 'customer/predict_churn.html', {'result':result })