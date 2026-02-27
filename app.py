import streamlit as st
from mainNeed.loader import load_data
from mainNeed.calorie import (
    calculate_bmi,
    get_bmi_category,
    calculate_calories
)
from mainNeed.workout import recommend_workout
from mainNeed.meal import recommend_meals


df, meal_df = load_data()

st.set_page_config(page_title="AI Fitness Planner", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏋️ AI Personalized Fitness Planner")
st.write("Smart workout and diet plan based on your body and goals.")

st.sidebar.header("Enter Your Details")

age = st.sidebar.number_input("Age", min_value=15, max_value=60, value=None)
gender = st.sidebar.selectbox("Gender", ["Select", "Male", "Female"])
weight = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=150.0, value=None)
height = st.sidebar.number_input("Height (m)", min_value=1.0, max_value=2.5, value=None)
goal = st.sidebar.selectbox("Goal", ["Select", "Fat Loss", "Muscle Gain", "Maintenance"])
experience = st.sidebar.selectbox("Experience", ["Select", "Beginner", "Intermediate", "Advanced"])
diet_type = st.sidebar.selectbox("Diet Type", ["Select", "Veg", "Non-Veg"])

generate = st.sidebar.button("Generate Plan 🚀")

if generate:

    if (
        age is None or
        weight is None or
        height is None or
        gender == "Select" or
        goal == "Select" or
        experience == "Select" or
        diet_type == "Select"
    ):
        st.warning("Please complete all fields.")
    else:
        bmi = calculate_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)
        calorie_target = calculate_calories(weight, height, age, gender, goal)

        st.subheader("Your Body Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("BMI", round(bmi, 2))
        col2.metric("Category", bmi_category)
        col3.metric("Daily Calories", round(calorie_target))

        st.progress(min(int(bmi * 3), 100))

        st.divider()

        workout_plan = recommend_workout(df, goal, experience)
        meal_plan = recommend_meals(meal_df, calorie_target, diet_type)

        with st.expander("🏋️ Recommended Workout Plan", expanded=True):
            st.dataframe(workout_plan, use_container_width=True)

        with st.expander("🥗 Recommended Meal Plan", expanded=True):
            st.dataframe(meal_plan, use_container_width=True)

        st.success("Your personalized plan is ready 💪")