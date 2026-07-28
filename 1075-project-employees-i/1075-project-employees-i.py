import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:

     return (project.merge(employee)
                    .rename(columns = {'experience_years':'average_years'})
                    .groupby('project_id')['average_years'].mean()
                    .round(2).reset_index())