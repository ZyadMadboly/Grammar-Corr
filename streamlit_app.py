import streamlit as st
import requests

st.title('Grammar Error Correction')
st.markdown('created by: *Yousef karam - Zeiad Madboly*')

inp = st.text_area("Enter Text", '')
submit = st.button('Check Your Text')

API_URL = "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if submit:
  output = query({
    "inputs": inp,
     "options": {
            "max_length": 3000  # Adjust the maximum length as per your requirement
  })
  st.write(output[0])
