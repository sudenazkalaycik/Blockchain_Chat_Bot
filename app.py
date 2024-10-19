import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


api_key = os.environ["GEMINI_API_KEY"]

genai.configure(api_key=api_key)