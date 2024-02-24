import os
from google.cloud import texttospeech
from helper.file_modes import MODE
from helper.split_text import split_text
from helper.synthesize_text import synthesize_text
from helper.file_saver import file_saver

def long_text_to_speech(input_file_path, language_code='de-DE', voice_name='de-DE-Standard-A', speaking_rate=1.0):
    # Initialize the client
    client = texttospeech.TextToSpeechClient.from_service_account_json("optimum-harbor-413518-fd425d99bf79.json")

    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into smaller parts
    chunks = split_text(text, max_length=2000)

    # Process each part and concatenate audio content
    audio_contents = [synthesize_text(client, chunk, language_code, voice_name, speaking_rate) for chunk in chunks]
    combined_audio = b''.join(audio_contents)

    # Save the combined audio to a file
    output_file_path = file_saver(input_file_path, combined_audio, MODE.TEXT_TO_SPEECH)

    print("Text to Speech done...")

    return output_file_path 