from dotenv import load_dotenv
load_dotenv()
import os
from langgraph.prebuilt import create_react_agent
from Tools.tools import *
from langchain_groq import ChatGroq

llm=ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

toolss=[
    get_time,
    calculator
]

agent=create_react_agent(model=llm,tools=toolss)

