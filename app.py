import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import personalities
# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )
# -----------------------------------
# Create Gemini client
# -----------------------------------
client = genai.Client(api_key=api_key)
# -----------------------------------
# Generate Gemini response
# -----------------------------------
def generate_response(question,pesona):
    # Get personality/system prompt
    system_prompt = personalities[pesona]
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=2000,
            system_instruction=system_prompt
        ),
        contents=question
    )
    return response.text
# -----------------------------------
# Test
# -----------------------------------
answer = generate_response("what is the difference between supervised and unsupervised learning?", "Friendly")
print(answer)