import streamlit as st
from groq import Groq

# 1. Page Config for a Pro Look
st.set_page_config(page_title="AI Polish Pro", page_icon="✨", layout="centered")

# 2. Custom CSS to make it "Glow"
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background: linear-gradient(45deg, #7f00ff, #e100ff);
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 20px rgba(127, 0, 255, 0.5);
    }
    .stTextArea textarea {
        border-radius: 15px;
        border: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. App Header
st.markdown("<h1 style='text-align: center; color: white;'>✨ AI Polish Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Transform your messy drafts into masterpiece content.</p>", unsafe_allow_html=True)

# 4. Connection
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 5. UI Layout
with st.container():
    user_input = st.text_area("Drop your messy notes here...", placeholder="e.g. tell boss i quit but make it nice", height=200)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        btn = st.button("Magic Polish ✨")

if btn:
    if user_input:
        with st.spinner("Polishing..."):
            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Rewrite this to be professional, engaging, and perfectly formatted: {user_input}"}],
                model="llama-3.3-70b-versatile",
            )
            st.markdown("---")
            st.subheader("✅ Result:")
            st.info(chat.choices[0].message.content)
            st.button("Copy to Clipboard (Coming Soon)")
    else:
        st.error("You gotta paste something first!")
