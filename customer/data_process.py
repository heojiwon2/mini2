def create_contract_end_soon_feature(data):
    if (data['contract'] == 'One year') & (data['tenure'] >= 11):
        data['contract_end_soon'] = 1
    elif (data['contract'] == 'Two year') & (data['tenure'] >= 23):
        data['contract_end_soon'] = 1
    elif data['contract'] == 'Month-to-month':
        data['contract_end_soon'] = 1
    else:
        data['contract_end_soon'] = 0
    return data

# 월별 요금 구간 생성
def categorize_monthly_charges(charges):
    if charges < 30:
        return 'Low'
    elif 30 <= charges < 70:
        return 'Medium'
    else:
        return 'High'
    
def categorize_tenure(tenure):
    if tenure < 12:
        return 'Short-term'
    elif 12 <= tenure < 36:
        return 'Medium-term'
    else:
        return 'Long-term'

def to_binary(data):
    binary_columns = ['gender', 'partner', 'dependents', 'phoneservice', 'paperlessbilling', 'seniorcitizen', 'partner+dependents_no', 'contract_end_soon', 'low_q1_total', 'low_q3_tenure','total_charges_binary_1500']

    for column in binary_columns:
        if data[column] in ['Yes', True, 1,'Male']:
            data[column] = 1
        else:
            data[column] = 0
    
    return data 

def do_1hot(data):
    object_columns = ['multiplelines', 'internetservice', 'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport', 'streamingtv', 'streamingmovies', 'contract', 'paymentmethod', 'monthly_charges_category', 'tenure_category']
    