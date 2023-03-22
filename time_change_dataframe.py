    df = ticker.history(period="1d", interval="1m")
    df.reset_index(inplace=True)
    df['Time_1'] = df['Datetime'].dt.time
    df = df[df['Time_1'] > pd.Timestamp('09:36:00').time()]
    print(df)
