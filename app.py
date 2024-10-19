import os
from dotenv import load_dotenv

import google.generativeai as genai

# .environ u çalıştırmak için bu fonksiyonu en başta çalıştırmamız gerekiyor.
load_dotenv()

# gemini bir LLM yani büyük dil modelidir.
api_key = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=api_key)

# dil modeli seçilir
model = genai.GenerativeModel("gemini-1.5-flash")

query = "Bana blokzinicirin ne olduğunu anlatır mısın?"
response = model.generate_content(query)

print(response.text)
