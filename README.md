# SKN03-3rd-6Team - 20%


# 👯‍♂️👯 멤버 소개 
| <img src="static/img/sad.png" height="200" width="200" /> | <img src="static/img/dis.png" height="200" width="200"  /> | <img src="static/img/happy.png" height="200" width="200" /> | <img src="static/img/envy.png" height="200" width="200"  /> | 
|:----------:|:----------:|:----------:|:----------:|
| 이준경(팀장) | 방효식 | 허지원 | 장수연 |   
| Django | 데이터분석(EDA)<br>FrontEnd | 데이터분석(EDA)<br>ML Model 구축 | 데이터분석(EDA)<br>FrontEnd| 



# 🖥️ 프로젝트 소개 
관리자를 위한 통계 데이터와 고객 이탈 예측 서비스 

## 페이지 소개
페이지는 크게 통계 분석페이지, 고객관리 페이지, 신규고객 페이지로 구성

### 통계 분석 페이지
<img src="static/img/EDA.png" height="200" width="1000" /><br>

1. 관리자 입장에서 업무에 필요한 지표를 상단의 CARD 형태로
2. 주요 대이터들에 대한 상관관계를 그래프로

### 고객 관리 페이지
<img src="static/img/customer.png" height="200" width="1000" /><br>

1. 학습시킨 모델을 pickle 파일을 이용해 django 서버에 load
2. 학습시킨 모델을 model.predict_proba()를 이용해 확률로 변환 후, 퍼센트에 따라 위험도 표시 및 색상
3. 고객 ID, 성별, 위험도에 따라 결과 필터링 기능 

#### 고객 디테일 페이지 

### 신규 고객 페이지

## 데이터 분석
<img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="Jupyter Logo" width="10"/>  [anal.ipynb](anal.ipynb)


### 앙상블 모델 

### 5개 요인 - 각 모델의 피쳐 중요도 중 상위 6개 중 겹치는 요인이 많은 변수로 선택 
- contract 기간 달마다, 1년, 2년 (범주형)
- monthly charges low medi high (범주형)
- tenure 기간 short medi long (범주형)
- fiber optic 사용자
- total charges 기준 : 1500 이하 (범주형)

### 5개 요인 검증 (로지스틱 회귀 선택)


## 👩🏻‍💻 개발 기간 및 기술 스택

### 2024.09.23 ~ 2023.09.24

### 기술 스택
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) 
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) 
![LightGBM](https://img.shields.io/badge/LightGBM-02569B?style=for-the-badge&logo=lightgbm&logoColor=white) 
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) 
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) 
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) 
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)







