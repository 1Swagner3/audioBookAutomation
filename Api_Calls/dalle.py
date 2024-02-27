import threading
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv
from Api_Calls.chat_gpt_generate_dalle_prompt import generate_dalle_prompt
from utils.file_modes import MODE
from utils.file_saver import file_saver
from utils.spinning_cursor import spinning_cursor

from utils.split_text import split_text

def generate_image(input_file_path):
    
    print("Start generating image...")

    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text_chunks = split_text(text)
    
    prompt = generate_dalle_prompt(text_chunks[0])
    
    # Set OpenAI API key
    load_dotenv()
    client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))
    
    # Create a threading event to control the spinner
    stop_event = threading.Event()

    # Start the spinner thread
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    print("Generating image ... ")
    spinner_thread.start()

    try:
        # Generate an image using DALL-E
        response = client.images.generate(
            model="dall-e-3", 
            prompt=prompt,
            quality="standard",
            n=1, 
            size="1792x1024"
        )
    finally:
        # Stop the spinner once the response is received
        stop_event.set()
        spinner_thread.join()


    # Get the image URL from the response
    image_url = response.data[0].url

    output_file_path = file_saver(input_file_path, image_url, MODE.IMAGE)

    print(f"Image saved to {output_file_path}")
