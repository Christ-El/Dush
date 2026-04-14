from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate 
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI( 
    model="gemini-2.5-flash",
    temperature=0.1,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([ 
    ("system", "you are helpful assistant that can answer qsions and help with tasks"),
    ("human", "{user_input}"),
])

chain = prompt | llm

while True:
    print("enter 'exit' to end the program")
    user_input = input("Enter a question: ")
    if user_input.lower() == "exit": 
        break
    response = chain.invoke({"user_input": user_input})
    print(response.content)