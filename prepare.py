import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def prep_telco(df):
    df = df.drop_duplicates()
    
    cols_to_drop = ['Unnamed: 0']
    df = df.drop(columns=cols_to_drop)
    
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
    
    dummy_df = pd.get_dummies(df[['gender','partner','dependents','phone_service','multiple_lines', 'online_security','device_protection','tech_support','streaming_tv','streaming_movies','paperless_billing','churn','contract_type','internet_service_type','payment_type', 'online_backup']], dummy_na=False, drop_first=[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True])
    
    dummy_df = dummy_df.rename(columns = {'gender_Male' : 'male', 'partner_Yes' : 'partner', 'dependents_Yes' : 'dependents', 'phone_service_Yes' : 'phone_service', 'multiple_lines_No phone service' : 'no_phone_service', 'multiple_lines_Yes' : 'multiple_lines', 'online_security_No internet service' : 'no_internet_service', 'online_security_Yes' : 'online_security', 'device_protection_Yes' : 'device_protection', 'tech_support_Yes' : 'tech_support', 'streaming_tv_Yes' : 'streaming_tv', 'streaming_movies_Yes' : 'streaming_movies', 'paperless_billing_Yes' : 'paperless', 'churn_Yes' : 'churn', 'contract_type_One year' : 'one_year', 'contract_type_Two year' : 'two_year', 'internet_service_type_Fiber optic' : 'fiber_optic', 'payment_type_Credit card (automatic)' : 'credit_card', 'payment_type_Electronic check' : 'electric_check', 'payment_type_Mailed check' : 'mailed_check', 'online_backup_Yes' : 'online_backup'})    
    
    dummy_df = dummy_df.drop(columns = ['no_phone_service', 'device_protection_No internet service', 'tech_support_No internet service', 'streaming_tv_No internet service', 'streaming_movies_No internet service', 'internet_service_type_None', 'online_backup_No internet service'])    
    
    new_df = df.drop(columns = ['customer_id', 'gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn', 'contract_type', 'internet_service_type', 'payment_type', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'online_backup'])    
    
    new_df = pd.concat([new_df, dummy_df], axis=1)

    new_df['live_alone'] = (new_df['partner'] == 0) & (new_df['dependents'] == 0)
    
    new_df['new_customer'] = new_df['tenure'] < 6
    
    return new_df


def split(df, stratify_by='churn'):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=319)
        train, validate = train_test_split(train, test_size=.3, random_state=319)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=319, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=319, stratify=train[stratify_by])
    
    return train, validate, test


