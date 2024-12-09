import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Handle invalid N (non-positive values)
    if N <= 0:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})
    
    # Remove duplicates to consider only distinct salary values
    unique_salaries = employee['salary'].drop_duplicates()

    # Sort salaries in descending order
    sorted_salaries = unique_salaries.sort_values(ascending=False)

    # Check if N is within the range of unique salaries
    if N > len(sorted_salaries):
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})

    # Get the Nth highest salary from the sorted list
    nth_highest = sorted_salaries.iloc[N - 1]  # Note: N-1 because pandas indexing is 0-based
    return pd.DataFrame({'getNthHighestSalary({})'.format(N): [nth_highest]})
