import pandas as pd

def recommend_workout(df, goal, experience):

    df["Workout_Type"] = df["Workout_Type"].astype(str).str.strip().str.lower()
    df["Experience_Level"] = df["Experience_Level"].astype(str).str.strip().str.lower()

    goal = goal.strip().lower()
    experience = experience.strip().lower()

    if goal == "fat loss":
        filtered = df[df["Workout_Type"].str.contains("cardio|hiit", na=False)]
    elif goal == "muscle gain":
        filtered = df[df["Workout_Type"].str.contains("strength", na=False)]
    else:
        filtered = df.copy()

    filtered = filtered[
        filtered["Experience_Level"].str.contains(experience, na=False)
    ]

    if filtered.empty:
        filtered = df.sample(5)

    return filtered[
        ["Name of Exercise", "Sets", "Reps",
         "Target Muscle Group", "Difficulty Level"]
    ].drop_duplicates().head(5)