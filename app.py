import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background:#0b1120;
}

/* HEADER */
.main-title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:white;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:35px;
}

/* CARD */
.card{
    background:#16213e;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 8px 25px rgba(0,0,0,.45);
    border:1px solid rgba(255,255,255,.08);
    margin-bottom:25px;
}

/* RESULT */
.result-card{
    background:linear-gradient(135deg,#10b981,#059669);
    padding:35px;
    border-radius:20px;
    text-align:center;
    color:white;
    box-shadow:0px 10px 35px rgba(16,185,129,.35);
}

/* BUTTON */
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#2563eb,#4f46e5);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:20px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0px 8px 20px rgba(37,99,235,.45);
}

/* Number Input */
.stNumberInput{
    background:#1e293b;
    border-radius:10px;
}

.metric-box{
    background:#1e293b;
    padding:15px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,.4);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("model.pkl")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=120)

    st.title("About")

    st.write("""
This ML model predicts the expected student score using:

- 📚 Hours Studied
- 😴 Sleep Hours
- 🎯 Attendance
- 📝 Previous Score

Model:
**KNeighborsRegressor**
""")

    st.info("Provide realistic values for better predictions.")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("<div class='main-title'>🎓 Student Performance Prediction</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Predict Academic Performance using Machine Learning</div>", unsafe_allow_html=True)

# -----------------------------
# INPUT CARD
# -----------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader("📋 Student Details")

left,right = st.columns(2)

with left:

    hours = st.number_input(
        "📚 Hours Studied",
        0.0,24.0,5.0,0.5
    )

    attendance = st.slider(
        "🎯 Attendance %",
        0,100,80
    )

with right:

    sleep = st.number_input(
        "😴 Sleep Hours",
        0.0,24.0,7.0,0.5
    )

    previous = st.slider(
        "📝 Previous Score",
        0,100,70
    )

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# METRICS
# -----------------------------
c1,c2,c3,c4 = st.columns(4)

c1.metric("📚 Study",f"{hours} hrs")
c2.metric("😴 Sleep",f"{sleep} hrs")
c3.metric("🎯 Attendance",f"{attendance}%")
c4.metric("📝 Previous",f"{previous}")

st.write("### 📊 Student Overview")

st.progress(attendance/100)

st.caption("Attendance Progress")

st.progress(sleep/10 if sleep<=10 else 1.0)

st.caption("Sleep Quality Indicator")

st.write("")

# -----------------------------
# BUTTON
# -----------------------------
predict = st.button("🚀 Predict Student Performance")

if predict:

    df = pd.DataFrame({

        "hours_studied":[hours],
        "sleep_hours":[sleep],
        "attendance_percent":[attendance],
        "previous_scores":[previous]

    })

    prediction = model.predict(df)[0]

    if prediction>=90:
        status="🌟 Excellent"
        color="green"

    elif prediction>=75:
        status="✅ Good"

    elif prediction>=60:
        status="📘 Average"

    else:
        status="⚠ Needs Improvement"

    st.markdown(f"""
    <div class="result-card">

# 🎯 Predicted Score

<h1 style="font-size:65px;">{prediction:.2f}</h1>

<h2>{status}</h2>

The model predicts the student's expected academic score based on the provided study habits and previous academic performance.

</div>
    """,unsafe_allow_html=True)

    st.write("")

    st.subheader("📌 Performance Insights")

    if attendance<75:
        st.warning("Increase attendance to improve performance.")

    if sleep<6:
        st.warning("Getting more sleep can improve learning.")

    if hours<4:
        st.warning("Increase study hours.")

    if previous<60:
        st.warning("Previous performance indicates additional preparation is needed.")

    if attendance>=90 and sleep>=7 and hours>=6:
        st.success("Excellent study habits detected!")

st.markdown("<div class='footer'>Built with ❤️ using Streamlit & Scikit-Learn</div>", unsafe_allow_html=True)
