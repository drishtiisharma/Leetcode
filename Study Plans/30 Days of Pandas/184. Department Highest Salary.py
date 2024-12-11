import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Find the highest salary for each department
    max_salary = employee.groupby('departmentId')['salary'].max().reset_index()

    # Merge with employee data to get the employees who have the highest salary
    result = pd.merge(employee, max_salary, how='inner', on=['departmentId', 'salary'])

    # Merge with department data to get the department names
    result = pd.merge(result, department, left_on='departmentId', right_on='id')[['name_y', 'name_x', 'salary']]

    # Rename columns for clarity
    result.columns = ['Department', 'Employee', 'Salary']
    
    return result
