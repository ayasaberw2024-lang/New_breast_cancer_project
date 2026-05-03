import streamlit as st
import requests

st.title("Breast Cancer Predictor")

inputs = []

for i in range(30):
    val = st.number_input(f"Feature {i}")
    inputs.append(val)

if st.button("Predict"):
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={f"f{i}": v for i, v in enumerate(inputs)}
    )

    st.write(response.json())