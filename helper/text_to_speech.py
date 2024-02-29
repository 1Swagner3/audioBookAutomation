from Api_Calls.elevenLabs_text_to_speech import elevenLabs_text_to_speech
from utils.split_text import split_text
from utils.file_saver import file_saver
from utils.file_modes import MODE
from pydub import AudioSegment

def text_to_speech(input_file_path):
    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into smaller parts
    chunks = split_text(text, max_length=2000)
    
    # Initialize an empty audio segment
    combined_audio = AudioSegment.empty()

    # Convert each chunk to audio and add to the combined audio
    for chunk in chunks:
        audio_segment = elevenLabs_text_to_speech(chunk)
        combined_audio += audio_segment

    # Use file_saver to save the combined audio
    output_file_path = file_saver(input_file_path, combined_audio, MODE.TEXT_TO_SPEECH)

    print("Text to Speech done...")
    return output_file_path
