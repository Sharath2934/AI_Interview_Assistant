import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant',layout='centered')
st.title('AI Interview Assistant')
st.caption('Practice interview with AI-generated questions and constructive feedback.')
st.caption('Launched by Sharath S')
st.write('Department of AI&DS')

try:
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.write("API connection successfull")
except (keyError, FileNotFoundError):
    st.error('GROQ_API_KEY is missing. Add it to Streamlit Cloud App setting')
    st.stop()
    role = st.selectbox("Select Job",[
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Machine learning Engineer",
        "HR Executive"
    ])
