## Integrate our code OpenAI API
import os
from constants import openai_key
os.environ["OPENAI_API_KEY"]=openai_key

# OpenAI API key
# api_key = "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"

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

print(chain.invoke({"topic": "ice cream"}) )
