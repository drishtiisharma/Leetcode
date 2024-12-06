import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_emailsdf=users[users['mail'].str.match('[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return valid_emailsdf
