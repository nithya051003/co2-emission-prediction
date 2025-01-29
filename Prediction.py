import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('final_random_forest_model.pkl')

# Function to predict CO₂ emissions
def predict_co2_emissions(engine_size, cylinders, fuel_consumption_comb):
    input_data = np.array([[engine_size, cylinders, fuel_consumption_comb]])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("CO₂ Emissions Prediction 🚗💨")
st.write("Enter car features to predict CO₂ emissions.")

# User input
engine_size = st.number_input("Engine Size (in Liters)", min_value=0.5, max_value=10.0, value=2.0, step=0.1)
cylinders = st.selectbox("Number of Cylinders", [3, 4, 5, 6, 8,10,12,16])
fuel_consumption_comb = st.number_input("fuel_consumption_comb", min_value=0.0, max_value=50.0, value=8.0, step=0.1)


# Prediction button
if st.button("Predict CO₂ Emissions"):
    result = predict_co2_emissions(engine_size, cylinders, fuel_consumption_comb)
    st.write(f"Predicted CO₂ Emissions: {result:.2f} g/km")

