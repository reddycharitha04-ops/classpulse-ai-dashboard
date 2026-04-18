import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="ClassPulse AI", layout="wide")

# -------------------------
# CUSTOM STYLING
# -------------------------
st.markdown("""
<style>
body {
    background-color: #F9FAFB;
}
.metric-card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    text-align: center;
}
.alert-box {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.red { background-color: #FEE2E2; color: #B91C1C; }
.yellow { background-color: #FEF3C7; color: #92400E; }
.green { background-color: #D1FAE5; color: #065F46; }
</style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
col1, col2, col3 = st.columns([6,2,2])

with col1:
    st.title("🧠 ClassPulse AI Dashboard")
    st.caption("DSA - Section A")

with col2:
    st.write("🔴 Live Class")

with col3:
    privacy = st.toggle("🔒 Privacy Mode")

# -------------------------
# MOCK DATA
# -------------------------
students = 60
engagement = np.random.randint(50, 100)
confusion = np.random.randint(10, 70)
attendance = np.random.randint(40, 60)
participation = np.random.randint(30, 90)

topics = ["Recursion", "Sorting", "Graphs", "DP"]
understanding = np.random.randint(30, 90, size=4)

# -------------------------
# METRICS ROW
# -------------------------
st.subheader("📊 Class Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Engagement", f"{engagement}%")
col2.metric("Confusion", f"{confusion}%")
col3.metric("Attendance", f"{attendance}/{students}")
col4.metric("Participation", f"{participation}%")

# -------------------------
# ALERTS
# -------------------------
st.subheader("🚨 Alerts")

if confusion > 60:
    st.markdown('<div class="alert-box red">⚠️ High confusion detected</div>', unsafe_allow_html=True)
elif confusion > 40:
    st.markdown('<div class="alert-box yellow">⚠️ Moderate confusion</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="alert-box green">✅ Class understanding is good</div>', unsafe_allow_html=True)

if engagement < 60:
    st.markdown('<div class="alert-box red">⚠️ Engagement dropped</div>', unsafe_allow_html=True)

# -------------------------
# MAIN GRID
# -------------------------
col1, col2 = st.columns(2)

# Concept understanding
with col1:
    st.subheader("📈 Concept Understanding")

    df = pd.DataFrame({
        "Topic": topics,
        "Understanding": understanding
    })

    fig = px.bar(df, x="Topic", y="Understanding", text="Understanding")
    st.plotly_chart(fig, use_container_width=True)

# Engagement timeline
with col2:
    st.subheader("⏳ Engagement Timeline")

    time_data = pd.DataFrame({
        "Time": [f"{i} min" for i in range(1, 11)],
        "Engagement": np.random.randint(50, 100, 10)
    })

    fig2 = px.line(time_data, x="Time", y="Engagement", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# SMART RECORDING
# -------------------------
st.subheader("🎥 Smart Recording Highlights")

st.info("10:05 → High confusion spike")
st.info("10:15 → Important explanation")
st.info("10:25 → Peak engagement")

# -------------------------
# AI SUGGESTIONS
# -------------------------
st.subheader("💡 AI Teaching Suggestions")

if confusion > 60:
    st.write("👉 Repeat the concept with simpler example")
elif engagement < 60:
    st.write("👉 Ask a question to re-engage students")
else:
    st.write("👉 Continue at current pace")

# -------------------------
# PRIVACY STATUS
# -------------------------
st.subheader("🔒 Privacy Mode Status")

if privacy:
    st.success("Running in privacy-safe mode (no camera)")
else:
    st.warning("Using multi-modal inputs (camera + interaction)")
