import pandas as pd

import env

sql = '''
select *
from customers
JOIN contract_types USING(`contract_type_id`)
JOIN internet_service_types USING(`internet_service_type_id`)
JOIN payment_types USING(payment_type_id);
'''

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

import os

import os

def get_telco_data():
    filename = "telco.csv"
    df = pd.read_csv(filename)
    return df  

