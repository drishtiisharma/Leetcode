import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result_df = customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name':'Customers'})
    return result_df
