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

def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(sql, get_connection('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_file(filename)

        # Return the dataframe to the calling code
        return df  

