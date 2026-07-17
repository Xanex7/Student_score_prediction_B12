import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Performance Prediction")
st.markdown(
    "Predict the student's expected score using study habits and academic history."
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------
st.subheader("Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "Hours Studied",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=0.5
    )

    attendance_percent = st.number_input(
        "Attendance (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=1.0
    )

with col2:
    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )

    previous_scores = st.number_input(
        "Previous Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Score", use_container_width=True):

    input_df = pd.DataFrame({
        "hours_studied": [hours_studied],
        "sleep_hours": [sleep_hours],
        "attendance_percent": [attendance_percent],
        "previous_scores": [previous_scores]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"🎯 Predicted Score: **{prediction:.2f}**")

    if prediction >= 90:
        st.balloons()
        st.info("🌟 Excellent Performance Expected!")
    elif prediction >= 75:
        st.info("👍 Good Performance Expected!")
    elif prediction >= 60:
        st.warning("📘 Average Performance Expected.")
    else:
        st.error("⚠ Student may require additional support.")
