import numpy as np
import pickle
import pandas as pd
import streamlit as st

model = pickle.load(open("model_XGB.pkl", "rb"))

teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele',
    'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill',
    'Hamilton', 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton',
    'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Cardiff', 'Chandigarh',
    'Adelaide', 'Bangalore', 'St Kitts', 'Christchurch', 'Trinidad'
]

st.title("Cricket Score Prediction")

batting_team = st.selectbox("Select the batting team", teams)
bowling_team = st.selectbox("Select the bowling team", teams)
city = st.selectbox("Select the city", cities)
current_score = st.number_input("Current score", min_value=0)
wickets = st.number_input("Wickets fallen", min_value=0, max_value=10)
overs = st.number_input("Overs completed", min_value=0.0, max_value=20.0, step=0.1)
extras = st.number_input("Extras", min_value=0.0)
last_five = st.number_input("Runs scored in the last 5 overs", min_value=0.0)

wickets_left = 10 - wickets
balls_left = 120 - (overs * 6)
crr = current_score / overs if overs > 0 else 0

if st.button("Predict"):
    if overs < 5:
        st.error("Overs completed must be greater than 5 for prediction.")
    elif batting_team == bowling_team:
        st.error("Batting Team and Bowling Team can't be the same")
    elif balls_left == 0 or wickets_left == 0:
        st.write(f"Score: {current_score}")
    else:
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'extras': [extras],
            'wickets_left': [wickets_left],
            'crr': [crr],
            'last_five': [last_five]
        })
        
        result = model.predict(input_df)
        output = int(result[0])
        st.write(f"Predicted Score: {output}")

if __name__ == "__main__":
    st.write("")

