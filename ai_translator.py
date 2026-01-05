from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()

st.title("AI Translator")
groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b",groq_proxy=groq_api_key)

generic_template = "Translate the following English to {language} without changing its meaning!"

prompt = ChatPromptTemplate(
    [
        ("system",generic_template),
        ("user","{text}")
    ]
)

parser = StrOutputParser()

chain = prompt | model | parser

language = st.text_input("Language you like to translate into...")
input_txt = st.text_input(f"Text you want to translate into {language}")


if input_txt:
    st.write(chain.invoke({"language":language,"text":input_txt}))