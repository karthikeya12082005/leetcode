import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id', as_index=False)['event_date'].min()
    df = df.rename(columns={'event_date': 'first_login'})
    return df
