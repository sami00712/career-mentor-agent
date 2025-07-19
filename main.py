import streamlit as st
from agents.career import get_career_roadmap  


st.set_page_config(page_title="Career Mentor AI", layout="centered")

# 💡 Custom CSS for better UI
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stTextInput>div>input {
        padding: 10px;
        border-radius: 8px;
    }
    .title-style {
        font-size: 36px;
        font-weight: bold;
        color: #2E8B57;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 🎯 Title
st.markdown('<div class="title-style">🎯 Career Mentor AI</div>', unsafe_allow_html=True)
st.markdown("#### Get a personalized career roadmap based on your dream field!")

# 📥 Input
career = st.text_input("What career are you interested in?", placeholder="e.g., Data Scientist, UI/UX Designer")

# 🚀 Button
if st.button("Generate Roadmap"):
    if not career.strip():
        st.warning("Please enter a valid career field.")
    else:
        with st.spinner("🚧 Building your career roadmap..."):
            roadmap = get_career_roadmap(career)
        
        st.success("✅ Roadmap generated successfully!")
        st.markdown("### 📌 Your Career Roadmap:")
        st.markdown(f"<div style='background-color:#f0f0f5;padding:15px;border-radius:10px;'>{roadmap}</div>", unsafe_allow_html=True)

# 📝 Footer
st.markdown("---")
st.caption("Built with ❤️ by Muhammad Sami Qaim Khnai")
