import streamlit as st
import google.generativeai as genai

# Streamlit securely reads the secret key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("My AI App")
user_input = st.text_input("Ask something:")

if user_input:
    response = model.generate_content(user_input)
    st.write(response.text)
