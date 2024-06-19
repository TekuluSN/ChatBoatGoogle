import google.generativeai as palm
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)

response = palm.chat(messages="hello")
      
print(response.last)

response = palm.generate_text(prompt="how are you")
      
print(response.result)