import streamlit as st
import pandas as pd
import joblib
import os

# Load the trained model pipeline
@st.cache_resource
def load_model():
    return joblib.load("models/rf_harness_model.pkl")

rf_pipeline = load_model()

st.set_page_config(
    page_title="Dog Harness Size Predictor",
    page_icon="🐶",
    layout="centered"
)

st.title("Dog Harness Size Predictor")
st.markdown("Upload details or enter manually to predict the harness size.")

# Manual Input
st.header("Enter Dog Details")

with st.form("dog_form"):
    breed = st.text_input("Breed", "Labrador")
    weight = st.number_input("Weight (kg)", min_value=1, max_value=100, value=20)
    chest = st.number_input("Chest (cm)", min_value=10, max_value=150, value=40)
    neck = st.number_input("Neck (cm)", min_value=5, max_value=80, value=25)
    bootsize = st.number_input("Boot Size", min_value=0, max_value=20, value=3)
    age = st.number_input("Age (years)", min_value=0, max_value=20, value=3)
    activity = st.selectbox("Activity Level", ["low", "medium", "high"])
    submit_button = st.form_submit_button("Predict Harness Size")

if submit_button:
    # Normalize categorical values to lowercase
    input_data = pd.DataFrame([{
        "breed": breed.lower(),
        "weight": weight,
        "chest": chest,
        "neck": neck,
        "bootsize": bootsize,
        "age": age,
        "activity": activity.lower()
    }])

    prediction = rf_pipeline.predict(input_data)[0]
    st.success(f"Predicted Harness Size: **{prediction}**")

# Uploading A CSV File
st.header("Or Upload A CSV File")
uploaded_file = st.file_uploader("Upload CSV with dog details", type=["csv"])

if uploaded_file is not None:
    new_data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data Preview:", new_data.head())

    try:
        # Ensure categorical columns are lowercase
        if "breed" in new_data.columns:
            new_data["breed"] = new_data["breed"].str.lower()
        if "activity" in new_data.columns:
            new_data["activity"] = new_data["activity"].str.lower()

        predictions = rf_pipeline.predict(new_data)
        new_data["predicted_harness_size"] = predictions
        st.success("Predictions Completed")

        st.dataframe(new_data)

        # Download Results
        csv = new_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download Predictions",
            data=csv,
            file_name="dog_harness_predictions.csv",
            mime="text/csv",
        )
    except Exception as e:
        st.error(f"Error: {e}")
