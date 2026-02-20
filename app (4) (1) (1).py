import streamlit as st
import nltk
import re
from nltk.sentiment import SentimentIntensityAnalyzer

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Student Feedback Analyzer",
    page_icon="🎓",
    layout="centered"
)

# -------------------------------
# Custom Dark Theme CSS
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    padding-top: 30px;
}
.card {
    background: linear-gradient(145deg, #111827, #020617);
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0px 12px 40px rgba(0,0,0,0.6);
    margin-bottom: 22px;
}
.title {
    font-size: 34px;
    font-weight: 800;
    text-align: center;
    color: #e5e7eb;
}
.subtitle {
    font-size: 16px;
    text-align: center;
    color: #9ca3af;
    margin-bottom: 28px;
}
.result {
    font-size: 24px;
    font-weight: 700;
    text-align: center;
    color: #f9fafb;
}
.badge {
    padding: 10px 18px;
    border-radius: 999px;
    font-weight: 700;
    display: inline-block;
    margin-top: 14px;
    font-size: 15px;
}
.excellent { background: #16a34a; color: #ecfdf5; }
.good { background: #0284c7; color: #e0f2fe; }
.average { background: #ca8a04; color: #fef9c3; }
.poor { background: #dc2626; color: #fee2e2; }
textarea {
    background-color: #020617 !important;
    color: #e5e7eb !important;
    border-radius: 12px !important;
    border: 1px solid #1e293b !important;
}
button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    height: 48px !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# NLTK Setup
# -------------------------------
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# -------------------------------
# Helper Functions
# -------------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def feedback_quality_percentage(text):
    text = clean_text(text)
    score = sia.polarity_scores(text)["compound"]
    percent = (score + 1) * 50
    return round(percent, 2)

# -------------------------------
# UI
# -------------------------------
st.markdown('<div class="title">🎓 Student Feedback Quality Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart sentiment-based quality analysis for student feedback</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

feedback = st.text_area(
    "✍️ Enter Student Feedback",
    height=150,
    placeholder="Example: The teaching was excellent and very interactive..."
)

analyze = st.button("🚀 Analyze Feedback", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# Results
# -------------------------------
if analyze:
    if feedback.strip():
        score = feedback_quality_percentage(feedback)

        if score >= 80:
            label = "Excellent 🌟"
            badge_class = "excellent"
        elif score >= 60:
            label = "Good 👍"
            badge_class = "good"
        elif score >= 40:
            label = "Average ⚖️"
            badge_class = "average"
        else:
            label = "Poor ❌"
            badge_class = "poor"

        st.markdown(f"""
        <div class="card">
            <div class="result">Quality Score: {score}%</div>
            <div style="text-align:center;">
                <span class="badge {badge_class}">{label}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter feedback text to analyze.")
