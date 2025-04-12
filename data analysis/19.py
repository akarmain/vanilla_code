import pandas as pd
from datetime import datetime, timedelta


def main():
    df = pd.read_csv('../imputs/actions.csv')

    df['date'] = df['date'].astype("datetime64[ns]")


    users_per_day = df.groupby('date')['ip'].nunique()
    print("ANS1:", users_per_day.idxmax())

    # ran =  df[df['date'].dt.month == 3]['ip'].nunique()
    ran = df[(df['date'].dt.month == 3) & (df['date'].dt.year == 2023)]

    print("ANS2:", ran)


    df['clicks'] = df['action'].str.split(',').apply(
        lambda actions: sum(1 for action in actions if action.strip() == 'click')
    )
    ran = df[(df['date'].dt.month == 3) & (df['date'].dt.year == 2023)]['clicks'].sum()
    print("ANS 3:", ran)

if __name__ == "__main__":
    main()
