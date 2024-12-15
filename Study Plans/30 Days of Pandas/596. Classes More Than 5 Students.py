import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    classcounts=courses.groupby('class')['student'].count().reset_index()
    result=classcounts[classcounts['student']>=5][['class']]
    return result
