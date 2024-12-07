import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank']=scores['score'].rank(ascending=False,method='dense').astype(int)
    # here the dense method is used instead of min cos it ensures the next rank after a tie is the next consecutive integer
    return scores.sort_values('score',ascending=False)[['score','rank']]
