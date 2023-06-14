import openai
import os
from dotenv import load_dotenv
import json



def generate_text(subject):
    load_dotenv()
    openai.api_key = os.getenv('CHAT_GPT_KEY')
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user", 
            "content": f"I'm making a post titled \"{subject}\" and I need eight brief points of information to teach someone about the subject. Each point should be around 15 words, and the total word count across all points should be around 135 words, a few more or less words is fine. Please format your response as a JSON object with the point number as the key and the information as the value. Each point should be a separate key-value pair in the JSON object. No newlines, please."
        }
    ]
    )
    print('progress: generated text')
    print(completion.choices[0].message.content)

    return json.loads(completion.choices[0].message.content)