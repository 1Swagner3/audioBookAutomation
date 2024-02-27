
import os
from dotenv import load_dotenv
import openai
import threading

from utils.spinning_cursor import spinning_cursor

def generate_dalle_prompt(text_chunk):
    load_dotenv()
    client = openai.OpenAI(api_key=os.environ.get("OPENAI_KEY"))

    # Start the spinner in a separate thread
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    print("Generating DALL-E prompt ... ")
    spinner_thread.start()

    try:
        # Generate a summary with ChatGPT
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text for a DALL-E image prompt, keeping in mind it's for a dark fantasy novel: {text_chunk} Also make sure not to violate open ai's content safety policy."}
            ]
        )

        # Stop the spinner
        stop_event.set()
        spinner_thread.join()

        # Access the response content
        if response.choices:
            summary = response.choices[0].message.content
        else:
            raise ValueError("Invalid response format or empty content")

        return summary

    except Exception as e:
        # Stop the spinner in case of an exception
        stop_event.set()
        spinner_thread.join()
        print(f"An error occurred: {e}")
        return None

