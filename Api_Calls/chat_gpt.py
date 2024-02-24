import os
import aiohttp
from dotenv import load_dotenv

async def get_improved_text(context_data):
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_KEY")

    # Ensure the API key is set
    if not openai_api_key:
        raise ValueError("OpenAI API key is not set in environment variables.")

    query = """
    This is a part of the dark fantasy novel that I am writing at the moment. 
    Improve the text so it reads like a professional novel but stay close to the original.
    Stay in german because the book is in german.
    """

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user", 
                "content": f"{query}\n{context_data}"
            }
        ],
        "max_tokens": 2000,
        "temperature": 0.2,
        "top_p": 1,
        "n": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    
    print("Calling OpenAI API...")
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            if response.status == 200:
                data = await response.json()

                # Extracting the response content
                if 'choices' in data and data['choices']:
                    choice = data['choices'][0]
                    if 'message' in choice and 'content' in choice['message']:
                        result = choice['message']['content'].strip()
                        return result
                    else:
                        raise Exception("No content found in the response message.")
                else:
                    raise Exception("Invalid response structure from OpenAI API.")
            else:
                response_body = await response.text()
                raise Exception(f"OpenAI API error: {response.status}, Response Body: {response_body}")
