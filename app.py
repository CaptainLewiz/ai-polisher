import streamlit as st
from groq import Groq

# 1. Setup the AI connection
# We will put the actual key in the "Secrets" box on the website later
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🚀 AI Writing Polisher")
st.write("Turn messy text into professional content instantly.")

# 2. The User Interface
user_input = st.text_area("Paste your messy text here:", height=200)

if st.button("Fix My Text ✨"):
    if user_input:
        with st.spinner("AI is working..."):
            # This sends your text to the Groq AI
            chat = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Rewrite this perfectly and professionally: {user_input}"}],
                model="llama-3.3-70b-versatile",
            )
            st.success("Done!")
            st.write(chat.choices[0].message.content)
    else:
        st.warning("Please paste some text first!")