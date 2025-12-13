import streamlit as st
import streamlit.components.v1 as components
import base64

st.title("Amazon Sales Analytics Dashboard [Power BI + Streamlit]")
st.write("Built an interactive Power BI dashboard to analyze Amazon sales across regions and categories.When Power BI asked for a Premium subscription to share the live link, I politely refused and outsmarted the problem by recording the dashboard and deploying it as a looping video inside a Streamlit app — because engineers don’t quit, they adapt. 😄Tools: Power BI, DAX, Streamlit, Python")
video_path = "Amazon.mp4"

with open(video_path, "rb") as video_file:
    video_bytes = base64.b64encode(video_file.read()).decode()

video_html = f"""
<video autoplay loop muted playsinline width="100%">
    <source src="data:video/mp4;base64,{video_bytes}" type="video/mp4">
</video>
"""

components.html(video_html, height=800)

