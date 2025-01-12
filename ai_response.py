import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv('C:\\Users\\asim_\\IdeaProjects\\wuw-bot\\config.env')
GEMINI_KEY = os.getenv('GEMINI_KEY')


class AIResponse:
    def get_ai_response(message):
        genai.configure(api_key=GEMINI_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content('ignore the !ask in the query: ' + message)
        return response.text


