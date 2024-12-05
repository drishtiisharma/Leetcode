import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid_tweetsdf=tweets[tweets['content'].str.len()>15]
    res=invalid_tweetsdf[['tweet_id']]
    return res
