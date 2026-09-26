import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

mensagens = [
    SystemMessage(content="Traduza o texto a seguir para inglês"),
    HumanMessage(content="O conhecimento muda o mundo")
]

modelo = ChatGoogleGenerativeAI(model="models/gemini-3.8-flash")
parser = StrOutputParser()
chain = modelo | parser

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}")
])

chain = template_mensagem | modelo | parser
