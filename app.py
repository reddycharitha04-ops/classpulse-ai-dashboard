import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

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
# MOCK DATA (SIMULATION)
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
# MULTI-MODAL INPUT STATUS
# -------------------------
st.subheader("🧠 Multi-Modal Understanding Engine")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("👁️ Face Signals", "Active" if not privacy else "Disabled")
col2.metric("📝 Quiz Data", "Active")
col3.metric("⏱️ Response Time", "Tracking")
col4.metric("🖱️ Activity", "Tracking")
col5.metric("🎤 Audio", "Listening")

# -------------------------
# OVERVIEW METRICS
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
st.subheader("🚨 Intelligent Alerts")

if confusion > 65:
    st.error("⚠️ High confusion detected across class")
elif confusion > 45:
    st.warning("⚠️ Moderate confusion emerging")
else:
    st.success("✅ Students understanding well")

if engagement < 60:
    st.error("⚠️ Engagement drop detected")

if participation < 40:
    st.warning("⚠️ Low participation")

# -------------------------
# CONCEPT ANALYTICS
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Concept-Level Understanding")

    df = pd.DataFrame({
        "Topic": topics,
        "Understanding": understanding
    })

    fig = px.bar(df, x="Topic", y="Understanding", text="Understanding")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("⏳ Engagement Timeline")

    time_data = pd.DataFrame({
        "Time": [f"{i} min" for i in range(1, 11)],
        "Engagement": np.random.randint(40, 100, 10)
    })

    fig2 = px.line(time_data, x="Time", y="Engagement", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# SMART RECORDING (CAMERA MODE)
# -------------------------
st.subheader("🎥 Smart Class Recording")

camera_mode = st.toggle("Enable Camera Mode")

if camera_mode:
    st.success("📷 Recording with AI analysis enabled")

    st.info("10:05 → High confusion moment")
    st.info("10:15 → Important explanation")
    st.info("10:25 → Peak engagement")

    st.write("🎯 Auto-generated revision clips available")

else:
    st.warning("Camera disabled → Using non-visual inputs")

# -------------------------
# ATTENDANCE INSIGHT
# -------------------------
st.subheader("🧾 Attendance + Engagement Insights")

st.write(f"📊 Attendance: {attendance}/{students}")

if attendance < 45:
    st.warning("Low attendance correlates with higher confusion")

# -------------------------
# DISTRACTION / ENGAGEMENT PATTERN
# -------------------------
st.subheader("📵 Engagement Pattern Detection")

if engagement < 60:
    st.error("⚠️ Overall class distraction detected")
else:
    st.success("✅ Class focused")

st.write("Tracking interaction drops, inactivity, and response gaps (privacy-safe)")

# -------------------------
# AI TEACHER ASSISTANCE
# -------------------------
st.subheader("💡 Real-Time Teaching Suggestions")

if confusion > 65:
    st.write("👉 Repeat concept with simpler explanation")
    st.write("👉 Give real-world example")
elif engagement < 60:
    st.write("👉 Ask interactive question")
    st.write("👉 Start quick quiz")
elif participation < 40:
    st.write("👉 Encourage student participation")
else:
    st.write("👉 Continue current pace")

# -------------------------
# HYBRID CLASSROOM STATUS
# -------------------------
st.subheader("🌐 Hybrid Classroom Monitoring")

st.write("👩‍🏫 Offline Students: 35")
st.write("💻 Online Students: 25")

st.success("Unified monitoring across physical + virtual classroom")

# -------------------------
# PRIVACY STATUS
# -------------------------
st.subheader("🔒 Privacy System")

if privacy:
    st.success("Privacy-safe mode active (no camera tracking)")
else:
    st.warning("Multi-modal mode active (camera + interaction)")
