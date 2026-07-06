import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = (transactions.groupby('account')['amount'].sum().reset_index(name  = 'balance'))
    return df[df.balance > 10_000].merge(users).iloc[:,[2,1]]