import openai
import os
from dotenv import load_dotenv
import json



def generate_topics(amount):
    load_dotenv()
    openai.api_key = os.getenv('CHAT_GPT_KEY')
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
                {
                    "role": "user", 
                    "content": f"Can you provide {amount} topics for one-minute videos? These videos should teach useful methods and built-in functions from popular programming languages. Avoid specific methods or functions, but do mention a language or framework. Specific methods will be requested later. Please respond in a JSON format with the following structure: {{\"summary\": \"one or two word summary of the topic\", \"value\": \"the topic\"}}."
                }
            ]
    )
    
    print('Progress: generated topics')
    print(completion.choices[0].message.content)

    return json.loads(completion.choices[0].message.content)