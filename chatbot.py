from dotenv import load_dotenv
import os
from google import genai
from google.genai import types


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

while(True):
    userResponse = input("You: ")

    if userResponse == "End":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction='''You are a chinese practice partner, respond 
            using HSK1 level chinese along with a translation. Respond in english
            when the user makes spelling or grammar mistakes explaining how they are
            incorrect. '''
        ),
        contents=userResponse,
    )

    print(response.text)
  

