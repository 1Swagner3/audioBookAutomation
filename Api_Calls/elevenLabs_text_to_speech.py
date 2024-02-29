import os
from dotenv import load_dotenv
import requests
from pydub import AudioSegment
import io

def elevenLabs_text_to_speech(text):
    load_dotenv()
    api_key = os.getenv("ELEVENLABS_API_KEY")

    url = "https://api.elevenlabs.io/v1/text-to-speech/qDodyvwFjkC72lo1EvXA"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    # Return the audio data as an AudioSegment object
    if response.ok:
        audio_data = io.BytesIO(response.content)
        return AudioSegment.from_file(audio_data, format="mp3")
    else:
        raise Exception(f"Error in text-to-speech conversion: {response.status_code}, {response.text}")
