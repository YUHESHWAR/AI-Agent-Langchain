from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

response = llm.invoke("What do you think about harry potter? give me the the answer in 20 words")

print(response.content)