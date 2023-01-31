import streamlit as st
from PIL import Image
import requests
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Context Similarity App", layout="centered")
st.image(image, caption='Context Similarity')
#
# page header
st.title(f"Context Similarity App")
with st.form("Extract"):
   text1 = st.text_input("Enter the texts to be compared separated by ;(semicolon) here")
   submit = st.form_submit_button("Determine Similarity")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/context-similarity-cf28e46c/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key SfMk1hJv.mVvJ1LaCpDRAkeTGG1spgnjcXcdDwLuP','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header 
        st.header("Context Similarity")
        # output results
        st.success(response.text.split("response\\")[1].replace(':','').replace('"','').replace('\\','').replace('}','').replace(']',''))