import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="🎓 AI Student Performance Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD MODEL
# ==========================================================

model = joblib.load("model.pkl")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
background:
linear-gradient(135deg,#050816,#08111f,#0b132b,#111827);
background-attachment:fixed;
}

.block-container{
padding-top:1rem;
padding-left:2rem;
padding-right:2rem;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#0f172a,#111827);
border-right:1px solid rgba(255,255,255,.08);
}

.card{
background:rgba(255,255,255,.06);
backdrop-filter:blur(18px);
border-radius:20px;
padding:25px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 15px 40px rgba(0,0,0,.35);
margin-bottom:20px;
transition:.35s;
}

.card:hover{
transform:translateY(-4px);
box-shadow:0 20px 50px rgba(0,0,0,.55);
}

.metricCard{
background:linear-gradient(145deg,#1e293b,#111827);
border-radius:18px;
padding:20px;
text-align:center;
box-shadow:0 10px 25px rgba(0,0,0,.45);
transition:.3s;
}

.metricCard:hover{
transform:scale(1.03);
}

.metricTitle{
color:#94a3b8;
font-size:15px;
}

.metricValue{
font-size:28px;
font-weight:700;
color:white;
margin-top:8px;
}

.bigTitle{
font-size:46px;
font-weight:700;
color:white;
}

.subtitle{
font-size:18px;
color:#cbd5e1;
margin-top:5px;
}

.resultCard{
background:linear-gradient(135deg,#1e293b,#0f172a);
padding:35px;
border-radius:22px;
box-shadow:0 20px 50px rgba(0,0,0,.45);
border:1px solid rgba(255,255,255,.08);
}

.tip{
background:#172554;
padding:14px;
border-radius:12px;
margin-bottom:10px;
color:white;
}

.good{
background:#052e16;
padding:16px;
border-radius:12px;
}

.warn{
background:#78350f;
padding:16px;
border-radius:12px;
}

.bad{
background:#450a0a;
padding:16px;
border-radius:12px;
}

.footer{
text-align:center;
color:#94a3b8;
padding:30px;
font-size:14px;
}

.predictButton button{

width:100%;
height:65px;

background:
linear-gradient(90deg,#2563eb,#7c3aed);

border:none;

border-radius:15px;

font-size:22px;

font-weight:bold;

color:white;

box-shadow:0 15px 35px rgba(37,99,235,.45);

transition:.3s;
}

.predictButton button:hover{

transform:scale(1.02);

background:
linear-gradient(90deg,#3b82f6,#8b5cf6);

}

div[data-testid="metric-container"]{
background:#111827;
padding:15px;
border-radius:15px;
border:1px solid rgba(255,255,255,.05);
box-shadow:0 8px 20px rgba(0,0,0,.3);
}

.stProgress > div > div > div > div{
background:
linear-gradient(90deg,#2563eb,#06b6d4);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=120
    )

    st.markdown("## 🎓 AI Student Dashboard")

    st.markdown("---")

    st.info("""

### Features

✅ Live Academic Evaluation

✅ Student Health Meter

✅ AI Recommendations

✅ Target Score Planner

✅ Machine Learning Prediction

✅ Pass / Fail Detection

✅ Performance Analysis

""")

    st.markdown("---")

    st.success("""

### Model Information

Algorithm

KNeighborsRegressor

Input Features

• Hours Studied

• Sleep Hours

• Attendance %

• Previous Score

Output

Predicted Student Score

""")

    st.markdown("---")

    st.caption("Built using ❤️ Streamlit & Scikit-Learn")

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""

<div class="card">

<div class="bigTitle">

🎓 AI Student Performance Dashboard

</div>

<div class="subtitle">

Predict student performance using Machine Learning while receiving
real-time academic evaluation, AI recommendations,
goal planning and performance insights.

</div>

</div>

""", unsafe_allow_html=True)
# ==========================================================
# KPI CARDS
# ==========================================================

st.markdown("## 📊 Dashboard Overview")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">🤖 Algorithm</div>
        <div class="metricValue">KNN</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">📊 Features</div>
        <div class="metricValue">4</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">⚡ Prediction</div>
        <div class="metricValue">Real-Time</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown("""
    <div class="metricCard">
        <div class="metricTitle">🎯 Status</div>
        <div class="metricValue">Ready</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# INPUT SECTION
# ==========================================================

st.markdown("""
<div class="card">

<h2 style="color:white;">
📝 Student Information
</h2>

<p style="color:#cbd5e1;">
Move the sliders to update the live academic evaluation.
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns(2)

with left:

    hours_studied = st.slider(
        "📚 Hours Studied",
        0,24,6
    )

    attendance_percent = st.slider(
        "🎯 Attendance (%)",
        0,100,80
    )

with right:

    sleep_hours = st.slider(
        "😴 Sleep Hours",
        0,12,7
    )

    previous_scores = st.slider(
        "📝 Previous Score",
        0,100,70
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# LIVE STUDENT SUMMARY
# ==========================================================

st.subheader("📋 Student Summary")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "📚 Study",
    f"{hours_studied} hrs"
)

c2.metric(
    "😴 Sleep",
    f"{sleep_hours} hrs"
)

c3.metric(
    "🎯 Attendance",
    f"{attendance_percent}%"
)

c4.metric(
    "📝 Previous",
    f"{previous_scores}%"
)

st.markdown("---")

# ==========================================================
# LIVE ACADEMIC EVALUATION
# ==========================================================

study = min(hours_studied/10*100,100)

sleep = 100 if 7<=sleep_hours<=9 else max(40,100-abs(8-sleep_hours)*15)

attendance = attendance_percent

previous = previous_scores

overall = (
    study +
    sleep +
    attendance +
    previous
)/4

st.subheader("📈 Live Academic Health")

st.progress(overall/100)

if overall>=90:

    st.success("🌟 Outstanding Academic Profile")

elif overall>=75:

    st.info("✅ Good Academic Profile")

elif overall>=60:

    st.warning("⚠ Average Academic Profile")

else:

    st.error("❌ Needs Improvement")

# ==========================================================
# LIVE DASHBOARD
# ==========================================================

a,b = st.columns(2)

with a:

    st.metric(
        "📚 Study Quality",
        f"{study:.0f}%"
    )

    st.progress(study/100)

    st.metric(
        "😴 Sleep Quality",
        f"{sleep:.0f}%"
    )

    st.progress(sleep/100)

with b:

    st.metric(
        "🎯 Attendance",
        f"{attendance:.0f}%"
    )

    st.progress(attendance/100)

    st.metric(
        "📝 Previous Performance",
        f"{previous:.0f}%"
    )

    st.progress(previous/100)

st.markdown("---")

# ==========================================================
# STAR RATING
# ==========================================================

if overall>=90:

    stars="⭐⭐⭐⭐⭐"

elif overall>=75:

    stars="⭐⭐⭐⭐"

elif overall>=60:

    stars="⭐⭐⭐"

elif overall>=40:

    stars="⭐⭐"

else:

    stars="⭐"

st.subheader("⭐ Academic Rating")

st.markdown(
f"## {stars}"
)

# ==========================================================
# LIVE RECOMMENDATIONS
# ==========================================================

st.subheader("💡 Live Recommendations")

tips=[]

if hours_studied<6:

    tips.append("📚 Increase study time to at least 6–8 hours/day.")

if sleep_hours<7:

    tips.append("😴 Sleep at least 7–8 hours every night.")

if attendance_percent<85:

    tips.append("🎯 Maintain attendance above 85%.")

if previous_scores<70:

    tips.append("📝 Improve previous academic performance.")

if not tips:

    st.success(
        "🎉 Excellent habits! Keep maintaining consistency."
    )

else:

    for tip in tips:

        st.markdown(
            f"""
            <div class="tip">
            {tip}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)
# ==========================================================
# TARGET SCORE PLANNER
# ==========================================================

st.markdown("---")

st.markdown("""
<div class="card">
<h2 style="color:white;">🎯 AI Target Score Planner</h2>
<p style="color:#cbd5e1;">
Select your desired score and get personalized academic recommendations.
</p>
</div>
""", unsafe_allow_html=True)

target_score = st.slider(
    "🎯 Desired Score",
    min_value=40,
    max_value=100,
    value=80
)

# ----------------------------------------------------------
# Recommendation Logic
# ----------------------------------------------------------

if target_score >= 90:

    rec_study = "8 - 10 Hours / Day"
    rec_sleep = "7 - 8 Hours"
    rec_attendance = "95 - 100 %"
    rec_previous = "85 % +"
    difficulty = "⭐⭐⭐⭐⭐"
    diff_color = "#16a34a"

elif target_score >= 80:

    rec_study = "6 - 8 Hours / Day"
    rec_sleep = "7 - 8 Hours"
    rec_attendance = "90 % +"
    rec_previous = "75 % +"
    difficulty = "⭐⭐⭐⭐"
    diff_color = "#2563eb"

elif target_score >= 70:

    rec_study = "5 - 6 Hours / Day"
    rec_sleep = "7 Hours"
    rec_attendance = "85 % +"
    rec_previous = "65 % +"
    difficulty = "⭐⭐⭐"
    diff_color = "#f59e0b"

elif target_score >= 60:

    rec_study = "4 - 5 Hours / Day"
    rec_sleep = "7 Hours"
    rec_attendance = "80 % +"
    rec_previous = "55 % +"
    difficulty = "⭐⭐"
    diff_color = "#fb923c"

else:

    rec_study = "3 - 4 Hours / Day"
    rec_sleep = "7 Hours"
    rec_attendance = "75 % +"
    rec_previous = "45 % +"
    difficulty = "⭐"
    diff_color = "#dc2626"

# ==========================================================
# TARGET DASHBOARD
# ==========================================================

st.subheader("📋 Recommended Academic Plan")

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "📚 Study",
        rec_study
    )

with p2:
    st.metric(
        "😴 Sleep",
        rec_sleep
    )

with p3:
    st.metric(
        "🎯 Attendance",
        rec_attendance
    )

with p4:
    st.metric(
        "📝 Previous Score",
        rec_previous
    )

st.markdown("---")

st.subheader("⭐ Goal Difficulty")

st.markdown(
f"""
<h2 style="color:{diff_color};">
{difficulty}
</h2>
""",
unsafe_allow_html=True
)

# ==========================================================
# GOAL GAP ANALYSIS
# ==========================================================

st.subheader("📈 Goal Gap Analysis")

gap1, gap2 = st.columns(2)

with gap1:

    st.write("### Current")

    st.write(f"📚 Study : **{hours_studied} hrs**")

    st.write(f"😴 Sleep : **{sleep_hours} hrs**")

    st.write(f"🎯 Attendance : **{attendance_percent}%**")

    st.write(f"📝 Previous Score : **{previous_scores}%**")

with gap2:

    st.write("### Recommended")

    st.write(f"📚 {rec_study}")

    st.write(f"😴 {rec_sleep}")

    st.write(f"🎯 {rec_attendance}")

    st.write(f"📝 {rec_previous}")

st.markdown("---")

# ==========================================================
# GOAL READINESS
# ==========================================================

goal = 0

if target_score >= 90:

    if hours_studied >= 8:
        goal += 25

    if 7 <= sleep_hours <= 8:
        goal += 25

    if attendance_percent >= 95:
        goal += 25

    if previous_scores >= 85:
        goal += 25

elif target_score >= 80:

    if hours_studied >= 6:
        goal += 25

    if 7 <= sleep_hours <= 8:
        goal += 25

    if attendance_percent >= 90:
        goal += 25

    if previous_scores >= 75:
        goal += 25

elif target_score >= 70:

    if hours_studied >= 5:
        goal += 25

    if sleep_hours >= 7:
        goal += 25

    if attendance_percent >= 85:
        goal += 25

    if previous_scores >= 65:
        goal += 25

else:

    if hours_studied >= 4:
        goal += 25

    if sleep_hours >= 7:
        goal += 25

    if attendance_percent >= 75:
        goal += 25

    if previous_scores >= 50:
        goal += 25

st.subheader("🎯 Goal Readiness")

st.progress(goal/100)

if goal == 100:

    st.success("🎉 Excellent! You are currently on track for your target score.")

elif goal >= 75:

    st.info("👍 You're close to achieving your target. A few improvements can help.")

elif goal >= 50:

    st.warning("⚠ Moderate readiness. Try improving the highlighted areas.")

else:

    st.error("❌ Significant improvements are needed to reach your target.")

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
# ==========================================================
# MACHINE LEARNING PREDICTION
# ==========================================================

if predict:

    input_df = pd.DataFrame({

        "hours_studied":[hours_studied],

        "sleep_hours":[sleep_hours],

        "attendance_percent":[attendance_percent],

        "previous_scores":[previous_scores]

    })

    prediction = float(model.predict(input_df)[0])

    prediction = max(0,min(100,prediction))

    # ==========================================================
    # PERFORMANCE LEVEL
    # ==========================================================

    if prediction>=90:

        level="🏆 Outstanding"

        level_color="#16a34a"

        stars="⭐⭐⭐⭐⭐"

        confidence=98

    elif prediction>=80:

        level="🌟 Excellent"

        level_color="#22c55e"

        stars="⭐⭐⭐⭐"

        confidence=95

    elif prediction>=70:

        level="✅ Good"

        level_color="#3b82f6"

        stars="⭐⭐⭐"

        confidence=92

    elif prediction>=60:

        level="🙂 Average"

        level_color="#f59e0b"

        stars="⭐⭐"

        confidence=88

    elif prediction>=40:

        level="⚠ Needs Improvement"

        level_color="#f97316"

        stars="⭐"

        confidence=85

    else:

        level="❌ Poor"

        level_color="#dc2626"

        stars="⭐"

        confidence=82

    # ==========================================================
    # PASS FAIL
    # ==========================================================

    PASS_MARK=40

    if prediction>=PASS_MARK:

        result="✅ PASS"

        result_color="#22c55e"

    else:

        result="❌ FAIL"

        result_color="#ef4444"

    # ==========================================================
    # CELEBRATION
    # ==========================================================

    if prediction>=90:

        st.balloons()

    # ==========================================================
    # RESULT HEADER
    # ==========================================================

    st.markdown("---")

    st.markdown(f"""

    <div class="resultCard">

    <h1 style="color:white;text-align:center;">

    🎯 Prediction Result

    </h1>

    <h1 style="

    font-size:80px;

    text-align:center;

    color:#60a5fa;

    ">

    {prediction:.2f}

    </h1>

    <h2 style="

    color:{level_color};

    text-align:center;

    ">

    {level}

    </h2>

    <h2 style="

    color:{result_color};

    text-align:center;

    ">

    {result}

    </h2>

    </div>

    """,unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    # ==========================================================
    # SCORE PROGRESS
    # ==========================================================

    st.subheader("📊 Prediction Score")

    st.progress(prediction/100)

    # ==========================================================
    # METRICS
    # ==========================================================

    a,b,c,d=st.columns(4)

    a.metric(

        "🎯 Predicted Score",

        f"{prediction:.2f}"

    )

    b.metric(

        "🏆 Performance",

        level

    )

    c.metric(

        "📈 Confidence",

        f"{confidence}%"

    )

    d.metric(

        "🎓 Result",

        result

    )

    st.markdown("---")

    # ==========================================================
    # AI PERFORMANCE ANALYSIS
    # ==========================================================

    st.subheader("🤖 AI Performance Analysis")

    left,right=st.columns(2)

    with left:

        st.success("### ✅ Strengths")

        if attendance_percent>=90:

            st.write("✔ Excellent Attendance")

        if previous_scores>=80:

            st.write("✔ Strong Academic Background")

        if hours_studied>=7:

            st.write("✔ Good Study Habits")

        if 7<=sleep_hours<=8:

            st.write("✔ Healthy Sleep Schedule")

    with right:

        st.error("### ⚠ Areas to Improve")

        if attendance_percent<90:

            st.write("• Improve Attendance")

        if previous_scores<80:

            st.write("• Improve Previous Scores")

        if hours_studied<7:

            st.write("• Increase Study Hours")

        if sleep_hours<7:

            st.write("• Sleep More")

    st.markdown("---")
        # ==========================================================
    # AI RECOMMENDATIONS
    # ==========================================================

    st.subheader("💡 Personalized AI Recommendations")

    recommendations = []

    if hours_studied < 6:
        recommendations.append(
            "📚 Increase study time to at least 6–8 hours daily."
        )

    if sleep_hours < 7:
        recommendations.append(
            "😴 Aim for 7–8 hours of quality sleep every night."
        )

    if attendance_percent < 85:
        recommendations.append(
            "🎯 Improve attendance above 85%."
        )

    if previous_scores < 70:
        recommendations.append(
            "📝 Strengthen core concepts to improve future performance."
        )

    if prediction < target_score:
        recommendations.append(
            f"📈 You are approximately {target_score-prediction:.1f} marks away from your target."
        )

    if prediction >= target_score:
        recommendations.append(
            "🏆 Congratulations! Your current profile is on track to achieve your target."
        )

    if len(recommendations)==1 and prediction>=target_score:
        st.success(recommendations[0])

    else:

        for tip in recommendations:

            st.info(tip)

    st.markdown("---")

    # ==========================================================
    # STUDENT REPORT CARD
    # ==========================================================

    st.subheader("📋 Student Academic Report")

    report = pd.DataFrame({

        "Parameter":[
            "Study Hours",
            "Sleep Hours",
            "Attendance",
            "Previous Score",
            "Predicted Score",
            "Performance",
            "Result"
        ],

        "Value":[
            f"{hours_studied} hrs/day",
            f"{sleep_hours} hrs/day",
            f"{attendance_percent} %",
            f"{previous_scores} %",
            f"{prediction:.2f}",
            level,
            result
        ]

    })

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================================================
    # OVERALL HEALTH SCORE
    # ==========================================================

    st.subheader("❤️ Overall Academic Health")

    health = (
        study +
        sleep +
        attendance +
        previous
    ) / 4

    st.progress(health/100)

    if health>=90:

        health_status="🟢 Excellent"

    elif health>=75:

        health_status="🔵 Good"

    elif health>=60:

        health_status="🟠 Average"

    else:

        health_status="🔴 Poor"

    st.metric(
        "Academic Health",
        f"{health:.1f}%",
        health_status
    )

    st.markdown("---")

    # ==========================================================
    # COMPARISON
    # ==========================================================

    st.subheader("🎯 Target vs Prediction")

    compare1,compare2=st.columns(2)

    with compare1:

        st.metric(
            "Desired Score",
            target_score
        )

    with compare2:

        st.metric(
            "Predicted Score",
            f"{prediction:.2f}",
            f"{prediction-target_score:.2f}"
        )

    if prediction>=target_score:

        st.success(
            "🎉 Great! According to the model, you are expected to meet or exceed your target."
        )

    else:

        st.warning(
            f"⚠ Increase your preparation to improve by about {target_score-prediction:.1f} marks."
        )

    st.markdown("---")

    # ==========================================================
    # PERFORMANCE BADGE
    # ==========================================================

    st.subheader("🏅 Achievement Badge")

    if prediction>=90:

        badge="🥇 Gold Scholar"

    elif prediction>=80:

        badge="🥈 Silver Scholar"

    elif prediction>=70:

        badge="🥉 Bronze Scholar"

    elif prediction>=60:

        badge="📘 Dedicated Learner"

    else:

        badge="📖 Keep Improving"

    st.markdown(
        f"## {badge}"
    )

    st.markdown("---")

    # ==========================================================
    # DOWNLOAD REPORT
    # ==========================================================

    csv = report.to_csv(index=False)

    st.download_button(

        "📄 Download Student Report",

        csv,

        file_name="student_prediction_report.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.markdown("---")
    # ==========================================================
    # VISUAL ANALYTICS
    # ==========================================================

    st.subheader("📊 Interactive Visual Analytics")

    col1, col2 = st.columns(2)

    with col1:

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction,
            number={"suffix": "%"},
            title={"text": "Predicted Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#3b82f6"},
                "steps": [
                    {"range": [0, 40], "color": "#fecaca"},
                    {"range": [40, 60], "color": "#fde68a"},
                    {"range": [60, 80], "color": "#bfdbfe"},
                    {"range": [80, 100], "color": "#bbf7d0"}
                ]
            }
        ))

        fig_gauge.update_layout(height=350)
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col2:

        health_score = (study + sleep + attendance + previous) / 4

        fig_health = go.Figure(go.Indicator(
            mode="gauge+number",
            value=health_score,
            number={"suffix": "%"},
            title={"text": "Academic Health"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#22c55e"},
                "steps": [
                    {"range": [0, 50], "color": "#fee2e2"},
                    {"range": [50, 75], "color": "#fef3c7"},
                    {"range": [75, 100], "color": "#dcfce7"}
                ]
            }
        ))

        fig_health.update_layout(height=350)
        st.plotly_chart(fig_health, use_container_width=True)

    st.markdown("---")

    st.subheader("📈 Feature Comparison")

    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        x=["Study", "Sleep", "Attendance", "Previous"],
        y=[study, sleep, attendance, previous],
        text=[
            f"{study:.0f}%",
            f"{sleep:.0f}%",
            f"{attendance:.0f}%",
            f"{previous:.0f}%"
        ],
        textposition="outside"
    ))

    fig_bar.update_layout(
        title="Student Academic Profile",
        height=450,
        yaxis=dict(range=[0, 100]),
        xaxis_title="Features",
        yaxis_title="Percentage"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    st.subheader("🕸️ Student Profile Radar")

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
        r=[
            study,
            sleep,
            attendance,
            previous,
            study
        ],
        theta=[
            "Study",
            "Sleep",
            "Attendance",
            "Previous",
            "Study"
        ],
        fill="toself",
        line=dict(width=3),
        name="Profile"
    ))

    radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=False,
        height=500
    )

    st.plotly_chart(radar, use_container_width=True)

    st.markdown("---")

    st.subheader("🏅 Performance Summary")

    s1, s2, s3 = st.columns(3)

    with s1:
        st.metric(
            "Prediction",
            f"{prediction:.2f}"
        )

    with s2:
        st.metric(
            "Academic Health",
            f"{health_score:.1f}%"
        )

    with s3:
        st.metric(
            "Target Gap",
            f"{abs(target_score - prediction):.1f}"
        )

    st.markdown("---")

    st.subheader("🤖 AI Final Verdict")

    if prediction >= 90:

        st.success("""
🏆 Outstanding Student

✅ Exceptional academic profile

✅ Very high probability of success

✅ Keep maintaining your consistency.
""")

    elif prediction >= 75:

        st.success("""
🌟 Excellent Student

✅ Strong preparation

✅ High academic potential

✅ Continue your current routine.
""")

    elif prediction >= 60:

        st.warning("""
🙂 Average Student

• Increase study hours

• Improve attendance

• Revise more consistently
""")

    else:

        st.error("""
⚠ Needs Improvement

• Study more regularly

• Improve attendance

• Strengthen weak subjects

• Follow the AI recommendations above
""")
            # ==========================================================
    # FINAL DASHBOARD INSIGHTS
    # ==========================================================

    st.markdown("---")

    st.subheader("🎓 Academic Summary")

    # Grade Calculation
    if prediction >= 90:
        grade = "A+"
    elif prediction >= 80:
        grade = "A"
    elif prediction >= 70:
        grade = "B"
    elif prediction >= 60:
        grade = "C"
    elif prediction >= 40:
        grade = "D"
    else:
        grade = "F"

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🎯 Grade", grade)

    with c2:
        st.metric("⭐ Rating", stars)

    with c3:
        st.metric("📈 Confidence", f"{confidence}%")

    with c4:
        st.metric("🏆 Result", result)

    st.markdown("---")

    # ==========================================================
    # TARGET PROGRESS
    # ==========================================================

    st.subheader("🎯 Progress Towards Target")

    progress = min((prediction / target_score) * 100, 100)

    st.progress(progress / 100)

    st.write(f"### {progress:.1f}% of Target Achieved")

    if progress >= 100:
        st.success("🎉 Congratulations! You have reached your target.")
    elif progress >= 80:
        st.info("🔥 You're very close to your target.")
    elif progress >= 60:
        st.warning("📚 Keep working consistently.")
    else:
        st.error("⚠ Significant improvement is needed.")

    st.markdown("---")

    # ==========================================================
    # AI INSIGHTS
    # ==========================================================

    st.subheader("🤖 AI Insights")

    insights = []

    if hours_studied >= 8:
        insights.append("📚 Excellent study routine.")

    if 7 <= sleep_hours <= 8:
        insights.append("😴 Healthy sleep schedule.")

    if attendance_percent >= 90:
        insights.append("🎯 Outstanding attendance.")

    if previous_scores >= 80:
        insights.append("📝 Strong previous academic performance.")

    if prediction >= 80:
        insights.append("🌟 High probability of excellent semester results.")

    if prediction < target_score:
        insights.append(
            f"📈 Increase your score by approximately {target_score-prediction:.1f} marks to reach your goal."
        )

    if len(insights) == 0:
        insights.append(
            "📖 Focus on improving your overall academic habits."
        )

    for item in insights:
        st.success(item)

    st.markdown("---")

    # ==========================================================
    # PERFORMANCE SCORECARD
    # ==========================================================

    st.subheader("📊 Performance Scorecard")

    scorecard = pd.DataFrame({

        "Category": [
            "Study",
            "Sleep",
            "Attendance",
            "Previous Score",
            "Prediction"
        ],

        "Score": [
            f"{study:.0f}%",
            f"{sleep:.0f}%",
            f"{attendance:.0f}%",
            f"{previous:.0f}%",
            f"{prediction:.2f}%"
        ]

    })

    st.dataframe(
        scorecard,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================================================
    # FINAL MESSAGE
    # ==========================================================

    st.markdown(f"""
    <div style="
        background:linear-gradient(135deg,#2563eb,#7c3aed);
        padding:30px;
        border-radius:20px;
        text-align:center;
        color:white;
        box-shadow:0 15px 35px rgba(0,0,0,.35);
    ">
        <h1>🎓 AI Evaluation Complete</h1>

        <h2>Predicted Score: {prediction:.2f}%</h2>

        <h2>{level}</h2>

        <h2>{result}</h2>

        <p>
        Keep learning, stay consistent, and continue improving every day.
        </p>

    </div>
    """, unsafe_allow_html=True)
    # ==========================================================
    # FOOTER
    # ==========================================================

    st.markdown("""

    <div class="footer">

    🎓 AI Student Performance Dashboard

    <br><br>

    Built with ❤️ using Streamlit, Pandas and Scikit-Learn

    </div>

    """,unsafe_allow_html=True)
