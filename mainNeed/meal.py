import pandas as pd

def recommend_meals(meal_df, calorie_target, diet_type):

    meal_df["diet_type"] = meal_df["diet_type"].astype(str).str.strip().str.lower()
    diet_type = diet_type.strip().lower()

    filtered = meal_df[
        meal_df["diet_type"].str.contains(diet_type, na=False)
    ]

    per_meal_calories = calorie_target / 3

    filtered = filtered[
        filtered["Calories"] <= per_meal_calories
    ]

    if filtered.empty:
        filtered = meal_df.sample(3)

    return filtered[
        ["meal_name", "Calories",
         "Proteins", "Carbs", "Fats", "prep_time_min"]
    ].head(3)