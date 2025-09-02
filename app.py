import time
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st
import altair as alt


# ---------- Page Config ----------
st.set_page_config(
	page_title="Baby Comfort Monitor",
	page_icon="👶",
	layout="wide",
)


# ---------- Sidebar Controls (Global) ----------
with st.sidebar:
	st.title("👶 Baby Comfort Monitor")
	st.caption("Demo dashboard")



# Helper to draw a small status badge
def status_badge(label: str, emoji: str, color: str) -> None:
	st.markdown(
		f"<span style='display:inline-block;padding:4px 8px;border-radius:8px;background:{color};color:#111;font-weight:600'>"
		f"{emoji} {label}</span>",
		unsafe_allow_html=True,
	)


# ---------- Header ----------
st.markdown("### 👶 Baby Vitals Panel")

col1, col2, col3, col4 = st.columns([1.2, 1.2, 1.6, 1.8])

with col1:
	st.metric(label="Skin Temperature", value="36.7 °C")
with col2:
	st.metric(label="Mat Temperature", value="28.5 °C")
with col3:
	status_badge("Expression Analysis: Happy/Comfortable", "🙂", "#C6F6D5")
with col4:
	status_badge("Sleep State: Sleeping peacefully", "💤", "#E6FFFA")

st.divider()


# ---------- Smart PCM Blanket Control ----------
st.markdown("### 🧊 Smart PCM Blanket Control")
pcm_col1, pcm_col2, pcm_col3 = st.columns([1, 1, 2])

with pcm_col1:
	st.write("**Current PCM State:** Melting (absorbing heat)")
with pcm_col2:
	adaptive_mode = st.toggle("Adaptive Mode", value=True)
	st.caption("Adaptive Mode: ✅ ON" if adaptive_mode else "Adaptive Mode: ❌ OFF")
with pcm_col3:
	manual_override = st.slider("Manual Override (target °C)", min_value=28, max_value=32, value=30)
	st.caption("Manual Override: Slider at 50% (28–32 °C)")

st.progress((manual_override - 28) / 4)

st.divider()


# ---------- Alert & Notification Center ----------
st.markdown("### 📡 Alert & Notification Center")

alert_col1, alert_col2 = st.columns([1.2, 2])
with alert_col1:
	status_badge("Status: Baby comfortable", "✅", "#C6F6D5")
	st.write("Recent Alert: ⚠ “Baby turned restless” (10 min ago)")
	st.write("Priority: 🟢 Low")

with alert_col2:
	alerts_df = pd.DataFrame(
		[
			{"Time": "09:45", "Alert": "Slight restlessness", "Priority": "Low"},
		]
	)
	st.dataframe(alerts_df, use_container_width=True, hide_index=True)

st.divider()


# ---------- Interactive Baby Avatar ----------
st.markdown("### 🎨 Interactive Baby Avatar")

avatar_expression = "🙂"  # Could be changed based on analysis
avatar_caption = "Smiling baby (updates with expression)"

avatar_col1, avatar_col2 = st.columns([1, 2])
with avatar_col1:
	st.markdown(
		f"<div style='font-size:72px;line-height:1'>{avatar_expression}</div>",
		unsafe_allow_html=True,
	)
	st.caption(avatar_caption)
with avatar_col2:
	st.write("Expression Analysis: Happy/Comfortable")
	st.write("Sleep State: Sleeping peacefully")

st.divider()


# ---------- Thermal Heat Map (Dummy Visualization) ----------
st.markdown("### 🔥 Thermal Heat Map")

zone_data = pd.DataFrame(
	{
		"Zone": ["A", "B", "C"],
		"Temperature": [37.2, 29.1, 27.9],
	}
)

# Create a dummy heatmap-like bar chart using Altair (simple and lightweight)
heat_chart = (
	alt.Chart(zone_data)
		.mark_bar()
		.encode(
			x=alt.X("Zone:N", title="Zone"),
			y=alt.Y("Temperature:Q", title="Temperature (°C)"),
			color=alt.Color(
				"Temperature:Q",
				scale=alt.Scale(scheme="redblue"),
				title="°C",
			),
			tooltip=["Zone", "Temperature"],
		)
		.properties(height=200)
)

st.altair_chart(heat_chart, use_container_width=True)
st.caption("Heat map shows mostly white (stable & safe).")

st.divider()


# ---------- Care Timeline Tracker ----------
st.markdown("### 📈 Care Timeline Tracker")

timeline_df = pd.DataFrame(
	[
		{"Time": "09:00", "Event": "Baby placed on mat"},
		{"Time": "09:15", "Event": "PCM warmed up → 28 °C"},
		{"Time": "09:30", "Event": "Baby fell asleep 🙂"},
		{"Time": "09:45", "Event": "Alert: slight restlessness ⚠"},
		{"Time": "10:00", "Event": "Comfort Score: 92/100"},
	]
)
st.dataframe(timeline_df, use_container_width=True, hide_index=True)

st.divider()




# ---------- Predictive Comfort Score (AI Dummy) ----------
st.markdown("### 🤖 Predictive Comfort Score")

score_col1, score_col2, score_col3 = st.columns([1, 1, 2])
with score_col1:
	st.metric("Comfort Score", "92/100")
with score_col2:
	status_badge("Risk Level: Low", "🟢", "#C6F6D5")
with score_col3:
	st.info("Prediction: “Baby likely to remain stable for the next 30 minutes.”")


st.divider()


# ---------- Energy-Free Impact Tracker ----------
st.markdown("### 🌍 Energy-Free Impact Tracker")

impact_col1, impact_col2 = st.columns([1, 2])
with impact_col1:
	st.metric("Electricity Saved", "0.5 kWh", help="Estimated for last 1 hour")
	st.metric("Equivalent to", "⚡ Charging a phone 10 times")
with impact_col2:
	impact_df = pd.DataFrame({
		"Time": ["09:00", "09:15", "09:30", "09:45", "10:00"],
		"kWh Saved": [0.00, 0.10, 0.25, 0.40, 0.50],
	})
	impact_chart = (
		alt.Chart(impact_df)
		.mark_line(point=True)
		.encode(x="Time:N", y="kWh Saved:Q", tooltip=["Time", "kWh Saved"])
		.properties(height=200)
	)
	st.altair_chart(impact_chart, use_container_width=True)


