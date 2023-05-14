import streamlit as st
import requests
from happytransformer import HappyTextToText
from happytransformer import TTSettings

st.title('Grammar Error Correction')
st.header('Using Attention Mechanism')
st.markdown('created by: *Yousef karam - Zeiad Madboly*')

inp = st.text_area("Enter Text", '')
submit = st.button('Check Your Text')
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=150)
input_text_1 = f"grammar: {inp}"
output_text_1 = happy_tt.generate_text(input_text_1, args=beam_settings)
st.write(output_text_1.text)

# st.title('Grammar Error Correction')
# st.header('Using Attention Mechanism')
# st.markdown('created by: *Yousef karam - Zeiad Madboly*')

# inp = st.text_area("Enter Text", '')
# submit = st.button('Check Your Text')

# API_URL = "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

# if submit:
#   output = query({
#     "inputs": inp,
#   })
#   st.write(output[0])
