import pandas as pd


def preprocess_summer(df, region_df):
    df_summer = df[df['Season'] == 'Summer']
    df_summer = df_summer.merge(region_df, on='NOC', how='left')
    df_summer.drop_duplicates(inplace=True)
    df_summer = pd.concat([df_summer, pd.get_dummies(df['Medal'])], axis=1)
    return df_summer


def preprocess_winter(df, region_df):
    df_winter = df[df['Season'] == 'Winter']
    df_winter = df_winter.merge(region_df, on='NOC', how='left')
    df_winter.drop_duplicates(inplace=True)
    df_winter = pd.concat([df_winter, pd.get_dummies(df['Medal'])], axis=1)
    return df_winter
