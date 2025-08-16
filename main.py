import os
import sys

from dotenv import load_dotenv
from google import genai

try:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=sys.argv[1]
    )
except Exception as e:
    print(e)
    sys.exit(1)
