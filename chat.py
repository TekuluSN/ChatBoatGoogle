import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)
st.title("TECHNOLOGIES") 
st.header("Chat with GoogleGenerativeAi") 
def main():
    text = st.empty()
    input_prompt = text.text_input('Enter input', placeholder="Prompt")
    bt = st.button("SEND", use_container_width=True)
    if bt and input_prompt:
        model = "models/text-bison-001"    #This is the only model currently available
        response = palm.generate_text(
            model=model,
            prompt=input_prompt,
            temperature=1,
            max_output_tokens=1024
        )
        st.write("")
        st.subheader("Response")
        st.header(response.result)
        st.write("")
        

       
    



if __name__=="__main__":
    main()