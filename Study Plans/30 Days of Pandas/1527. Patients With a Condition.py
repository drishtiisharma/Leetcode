import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diab = patients[patients['conditions'].str.contains(r'(^|\s)' + "DIAB1" + r'(\w*|\s\w+)*(\s|\b)')]
    return diab
