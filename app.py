import streamlit as st
import numpy as np
import pickle

# Load model (baad me save karenge)
model = pickle.load(open('model.pkl', 'rb'))

st.title("Customer Churn Prediction")

# Inputs
tenure = st.number_input("Tenure")
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

# Prediction
if st.button("Predict"):
    input_data = np.array([[tenure, monthly_charges, total_charges]])
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")