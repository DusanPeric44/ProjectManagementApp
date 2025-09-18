import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")

#Developer form
st.header("Add a developer")
dev_name = st.text_input("Developer name")
dev_experience = st.number_input("Experience (Years)", min_value=0, max_value=50, value=0)

if st.button("Create developer"):
    dev_data = {
      "name": dev_name,
      "experience": dev_experience
    }
    response = requests.post("http://127.0.0.1:8000/developers/", json=dev_data)
    st.json(response.json())

#Create project form
#Project form