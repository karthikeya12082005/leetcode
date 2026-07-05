import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    grouped_Rides = rides.groupby('user_id').distance.sum().reset_index()
    merged = pd.merge(users, grouped_Rides, left_on='id', right_on='user_id', how='left').fillna(0)
    merged.rename(columns={'distance': 'travelled_distance'}, inplace=True)
    merged.drop('user_id', axis=1, inplace=True)
    merged.sort_values(by=['travelled_distance', 'name'], ascending=[False, True], inplace=True)
    merged.reset_index(drop=True, inplace=True)
    merged = merged[['name','travelled_distance']]
    return merged