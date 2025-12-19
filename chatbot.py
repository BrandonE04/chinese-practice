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
            incorrect. Start these messages with "ERROR:". Be active
            and make sure to ask questions to facilitate the conversation. Put your
            response in the following format:
            Chinese characters
            Pinyin
            English translation

            Example of response to correct user input "你好！":
            你好！
            nǐ hǎo!
            hello!

            Example of reponse to the incorrect user input "你号":
            ERROR: The phrase 你号 does not make sense, you were likely meaning to say 你好, as in hello.
            '''
        ),
        contents=userResponse,
    )

    lines = response.text.splitlines()

    if response.text[0:5] == "ERROR":
        error = response.text
    else:
        characters = lines[0]
        pinyin = lines[1]
        english = lines[2]
  

