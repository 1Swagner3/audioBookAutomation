import os
from openai import OpenAI
from dotenv import load_dotenv
def open_ai_text_to_speech(text, filename):
    load_dotenv()
    client = OpenAI(api_key=os.environ.get("OPENAI_KEY"))
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )
    
    response.stream_to_file(f"Output_Text_to_Speech/{filename}")
    print(f"Chunk saved as {filename}")
