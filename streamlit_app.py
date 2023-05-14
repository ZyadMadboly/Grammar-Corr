import streamlit as st
import requests

st.title('Grammar Error Correction')
st.header('Using Attention Mechanism')
st.markdown('created by: *Yousef karam - Zeiad Madboly*')

inp = st.text_area("Enter Text", '')
submit = st.button('Check Your Text')

API_URL = "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if submit:
  lines = inp.split('\n')
  corrected_lines = []
  for line in lines:
    corrected_line = query({
      "inputs": line,
    })[0]
    corrected_lines.append(corrected_line)
corrected_paragraph = '\n'.join([str(line) for line in corrected_lines])
st.write(corrected_paragraph)
