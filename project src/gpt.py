import openai
from const import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY
def genCompletion(query):                                       
    conversation = [
        {"role": "system", "content": "You are a good teacher. You help students with homework problems by giving them easy explanation and answers."},
        {"role": "user", "content": query},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply