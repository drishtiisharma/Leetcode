import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    #pd.melt() is a Pandas function used to "unpivot" or reshape a DataFrame from a wide format (many columns) to a long format (fewer columns).
    return pd.melt(
        products,id_vars='product_id',var_name='store',value_name='price'
    ).dropna() #dropna() is used to remove these rows where the price is NaN.
