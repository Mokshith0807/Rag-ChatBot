import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API Key Loaded:", bool(api_key))

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", temperature=0, google_api_key=api_key
)

response = llm.invoke("Say hello in one sentence.")

print("\nResponse:")
print(response.content)
