import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# #Langsmith tracking
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

os.environ["LANGCHAIN_API_KEY"] = st.secrets.get("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = st.secrets.get("LANGCHAIN_PROJECT", "Satvik_Chatbot")

#Prompt template
prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant of Satvik Kumar Nayak who is your master/owner has done his java fullstack using springboot as major and studying generative ai in his 2nd year at MIT bengaluru.please respond to the question asked "),
    ("user","Question: {question}")
])

OLLAMA_BASE_URL = st.secrets["OLLAMA_BASE_URL"]
#streamlit framework
st.title("Satvik's Personal AI chatbot")
input_text=st.text_input("What question you have in your mind?")

#model creation using ollama
llm = Ollama(
    model="gemma3:1b",
    base_url=OLLAMA_BASE_URL  # Connect to remote Ollama
)
output_parser=StrOutputParser()
chain= prompt|llm|output_parser

if (st.button("->") or input_text):
    st.write(chain.invoke({"question": input_text}))

