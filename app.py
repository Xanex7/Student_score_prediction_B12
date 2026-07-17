import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("model.pkl")

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

.stApp{
background: linear-gradient(135deg,#08111f,#0b132b,#111827);
background-attachment:fixed;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#111827,#0f172a);
border-right:1px solid rgba(255,255,255,0.08);
}

.block-container{
padding-top:1rem;
padding-left:2rem;
padding-right:2rem;
}

.title{
font-size:45px;
font-weight:700;
color:white;
margin-bottom:5px;
}

.subtitle{
font-size:18px;
color:#b8c1cc;
margin-bottom:30px;
}

.card{
background:rgba(255,255,255,.06);
padding:25px;
border-radius:18px;
border:1px solid rgba(255,255,255,.12);
backdrop-filter:blur(18px);
box-shadow:0 10px 35px rgba(0,0,0,.35);
margin-bottom:20px;
transition:.3s;
}

.card:hover{
transform:translateY(-3px);
box-shadow:0 15px 40px rgba(0,0,0,.55);
}

.metricCard{
background:linear-gradient(145deg,#1f2937,#111827);
padding:18px;
border-radius:15px;
text-align:center;
box-shadow:0 10px 25px rgba(0,0,0,.4);
}

.metricTitle{
font-size:16px;
color:#cbd5e1;
}

.metricValue{
font-size:28px;
font-weight:700;
color:white;
}

.predictButton button{
width:100%;
height:65px;
font-size:22px;
font-weight:bold;
border:none;
border-radius:15px;
background:linear-gradient(90deg,#2563eb,#7c3aed);
color:white;
transition:.3s;
box-shadow:0 10px 30px rgba(37,99,235,.5);
}

.predictButton button:hover{
transform:scale(1.02);
background:linear-gradient(90deg,#3b82f6,#8b5cf6);
}

.resultCard{
padding:30px;
border-radius:20px;
background:linear-gradient(135deg,#1e293b,#0f172a);
box-shadow:0px 15px 40px rgba(0,0,0,.45);
text-align:center;
border:1px solid rgba(255,255,255,.1);
}

.footer{
text-align:center;
padding:20px;
color:#94a3b8;
font-size:15px;
margin-top:40px;
}

.tip{
padding:12px;
border-radius:10px;
margin-bottom:10px;
background:#172554;
color:white;
}

.successBox{
background:#052e16;
padding:18px;
border-radius:15px;
}

.warningBox{
background:#78350f;
padding:18px;
border-radius:15px;
}

.errorBox{
background:#450a0a;
padding:18px;
border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=120
    )

    st.markdown("## 🎓 Student Predictor")

    st.write("---")

    st.info("""
This application predicts a student's expected academic score using Machine Learning.

### Features

✅ KNN Regression

✅ Real-time Prediction

✅ Performance Analysis

✅ Pass / Fail

✅ Personalized Tips

✅ Beautiful Dashboard
""")

    st.write("---")

    st.success("""
### Model Information

Algorithm : KNeighborsRegressor

Features Used

• Hours Studied

• Sleep Hours

• Attendance %

• Previous Score
""")

    st.write("---")

    st.caption("Made with ❤️ using Streamlit")

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    """
    <div class="card">
        <div class="title">🎓 Student Performance Prediction Dashboard</div>
        <div class="subtitle">
            Predict the student's academic performance using Machine Learning.
            Enter the student details below and click Predict.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# KPI CARDS
# ==========================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">🤖 Algorithm</div>
        <div class="metricValue">KNN</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">📊 Features</div>
        <div class="metricValue">4</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">🎯 Prediction</div>
        <div class="metricValue">Real-Time</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">⚡ Model</div>
        <div class="metricValue">Ready</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown(
    """
    <div class="card">
        <h2 style="color:white;">📝 Enter Student Information</h2>
        <p style="color:#b8c1cc;">
        Fill in the student's academic details for prediction.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2)

# -------------------------------
# LEFT COLUMN
# -------------------------------

with left:

    st.subheader("📚 Academic Information")

    hours_studied = st.slider(
        "Hours Studied",
        min_value=0,
        max_value=24,
        value=8,
        help="Average hours studied daily."
    )

    attendance_percent = st.slider(
        "Attendance Percentage",
        min_value=0,
        max_value=100,
        value=80,
        help="Overall attendance percentage."
    )

# -------------------------------
# RIGHT COLUMN
# -------------------------------

with right:

    st.subheader("💤 Personal Information")

    sleep_hours = st.slider(
        "Sleep Hours",
        min_value=0,
        max_value=12,
        value=7,
        help="Average sleep per day."
    )

    previous_scores = st.slider(
        "Previous Exam Score",
        min_value=0,
        max_value=100,
        value=70,
        help="Previous examination percentage."
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# SUMMARY CARDS
# ==========================================================

st.markdown("## 📊 Student Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📚 Study Hours", f"{hours_studied} hrs")

with c2:
    st.metric("😴 Sleep", f"{sleep_hours} hrs")

with c3:
    st.metric("🎯 Attendance", f"{attendance_percent}%")

with c4:
    st.metric("📝 Previous Score", f"{previous_scores}%")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# INPUT QUALITY
# ==========================================================

quality = 0

if hours_studied >= 6:
    quality += 25

if sleep_hours >= 7:
    quality += 25

if attendance_percent >= 85:
    quality += 25

if previous_scores >= 70:
    quality += 25

st.subheader("📈 Academic Readiness")

st.progress(quality / 100)

if quality >= 80:
    st.success("Excellent academic habits.")
elif quality >= 60:
    st.info("Good academic profile.")
elif quality >= 40:
    st.warning("Average academic profile.")
else:
    st.error("Poor academic profile.")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# PREDICT BUTTON
# ==========================================================

st.markdown('<div class="predictButton">', unsafe_allow_html=True)

predict = st.button(
    "🚀 Predict Student Performance",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)
