import pandas as pd

def load_data():
    df = pd.read_csv("data/Final_data.csv")
    meal_df = pd.read_csv("data/meal_metadata.csv")

    df = df.drop_duplicates()
    meal_df = meal_df.drop_duplicates()

    df = df.fillna(0)
    meal_df = meal_df.fillna(0)

    return df, meal_df