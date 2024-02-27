import os
from Api_Calls.open_ai_text_to_speech import open_ai_text_to_speech
from utils.file_modes import MODE
from utils.split_text import split_text
from utils.file_saver import file_saver
from pydub import AudioSegment

def text_to_speech(input_file_path):

    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into smaller parts
    chunks = split_text(text, max_length=4000)
    
    # Convert each chunk to audio
    audio_files = []
    for i, chunk in enumerate(chunks):
        filename = f"chunk_{i}.mp3"
        open_ai_text_to_speech(chunk, filename)
        audio_files.append(filename)

    # Combine the audio files
    combined_audio = AudioSegment.empty()
    for file in audio_files:
        sound = AudioSegment.from_mp3(f"Output_Text_to_Speech/{file}")
        combined_audio += sound
        
        # Delete the chunk file
        os.remove(f"Output_Text_to_Speech/{file}")

    # Save the combined audio to a file
    output_file_path = file_saver(input_file_path, combined_audio, MODE.TEXT_TO_SPEECH)

    print("Text to Speech done...")

    return output_file_path 