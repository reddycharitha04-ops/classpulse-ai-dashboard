import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="ClassPulse AI", layout="wide")

# -------------------------
# HEADER
# -------------------------
col1, col2, col3 = st.columns([6,2,2])

with col1:
    st.title("🧠 ClassPulse AI Dashboard")
    st.caption("DSA - Section A | Hybrid Classroom")

with col2:
    st.write("🔴 Live")

with col3:
    privacy = st.toggle("🔒 Privacy Mode")

# -------------------------
# VIDEO INPUT
# -------------------------
st.subheader("🎥 Upload Classroom Video")

uploaded_file = st.file_uploader("Upload a lecture video", type=["mp4", "mov", "avi"])

# -------------------------
# SIMULATED DATA
# -------------------------
students = 60
engagement = np.random.randint(40, 100)
confusion = np.random.randint(10, 80)
confidence = 100 - confusion

attendance = np.random.randint(40, 60)
participation = np.random.randint(30, 90)

topics = ["Recursion", "Sorting", "Graphs", "DP"]
understanding = np.random.randint(30, 90, size=4)

# -------------------------
# MULTI-MODAL ENGINE
# -------------------------
st.subheader("🧠 Multi-Modal Understanding Engine")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Face Signals", "Active" if not privacy else "Disabled")
col2.metric("Quiz Data", "Active")
col3.metric("Response Time", "Tracking")
col4.metric("Activity", "Tracking")
col5.metric("Audio", "Listening")

# -------------------------
# OVERVIEW
# -------------------------
st.subheader("📊 Class Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Engagement", f"{engagement}%")
col2.metric("Confusion", f"{confusion}%")
col3.metric("Confidence", f"{confidence}%")
col4.metric("Attendance", f"{attendance}/{students}")

# -------------------------
# ALERTS
# -------------------------
st.subheader("🚨 Alerts")

if confusion > 65:
    st.error("High confusion detected")
elif confusion > 45:
    st.warning("Moderate confusion")
else:
    st.success("Good understanding")

if engagement < 60:
    st.error("Engagement drop detected")

# -------------------------
# CONCEPT ANALYTICS
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Concept Understanding")
    df = pd.DataFrame({"Topic": topics, "Understanding": understanding})
    fig = px.bar(df, x="Topic", y="Understanding", text="Understanding")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("⏳ Engagement Timeline")
    timeline = list(range(1, 11))
    engagement_data = np.random.randint(40, 100, 10)
    df2 = pd.DataFrame({"Time": timeline, "Engagement": engagement_data})
    fig2 = px.line(df2, x="Time", y="Engagement", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# VIDEO ANALYSIS
# -------------------------
if uploaded_file is not None:
    st.subheader("📊 Video Analysis")
    st.video(uploaded_file)

    timeline = list(range(1, 11))
    engagement_timeline = np.random.randint(40, 100, 10)
    confusion_timeline = 100 - engagement_timeline + np.random.randint(0, 20, 10)

    col1, col2 = st.columns(2)

    with col1:
        df3 = pd.DataFrame({"Time": timeline, "Engagement": engagement_timeline})
        fig3 = px.line(df3, x="Time", y="Engagement", markers=True)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        df4 = pd.DataFrame({"Time": timeline, "Confusion": confusion_timeline})
        fig4 = px.line(df4, x="Time", y="Confusion", markers=True)
        st.plotly_chart(fig4, use_container_width=True)

    # Smart highlights
    st.subheader("🎯 Smart Recording Highlights")

    for i, val in enumerate(confusion_timeline):
        if val > 70:
            st.warning(f"{i+1} min → High confusion detected")

    st.info("Auto-generated learning highlights ready")

    # AI Suggestions
    st.subheader("💡 AI Suggestions")

    if np.mean(confusion_timeline) > 60:
        st.write("👉 Repeat difficult sections")
    elif np.mean(engagement_timeline) < 60:
        st.write("👉 Add interaction")
    else:
        st.write("👉 Continue teaching flow")

# -------------------------
# PRIVACY
# -------------------------
st.subheader("🔒 Privacy Status")

if privacy:
    st.success("Privacy-safe mode (no camera)")
else:
    st.warning("Camera-enabled mode")
