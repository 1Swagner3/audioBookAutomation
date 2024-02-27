from helper.file_modes import MODE
from helper.split_text import split_text
from helper.synthesize_voice import synthesize_voice
from helper.file_saver import file_saver

def long_text_to_speech(input_file_path):

    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into smaller parts
    chunks = split_text(text, max_length=2000)

    # Process each part and concatenate audio content
    audio_contents = [synthesize_voice(chunk) for chunk in chunks]
    combined_audio = b''.join(audio_contents)

    # Save the combined audio to a file
    output_file_path = file_saver(input_file_path, combined_audio, MODE.TEXT_TO_SPEECH)

    print("Text to Speech done...")

    return output_file_path 