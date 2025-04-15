import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

def get_sql_from_question(prompt: str):      #show me total sales in January
    response = model.generate_content(prompt) #the main content(text) candidates, safefy attributes, usage metadata, etc...
    return response.text   #sql query
