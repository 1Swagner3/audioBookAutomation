import asyncio
from Api_Calls.transcibe_audio import transcribe_audio
from Api_Calls.text_to_speech import long_text_to_speech
from Api_Calls.chat_gpt import get_improved_text
from helper.improve_text import improve_text


def main():
    
    # Get user input
    user_input = input("Please enter a google cloud storage: ")
    
    # Read audio file
    transcribed_text_file_path = transcribe_audio(user_input)

    # Process text
    improved_text_file_path = asyncio.run(improve_text(transcribed_text_file_path))
    # Convert processed text to speech
    speech_file = long_text_to_speech(improved_text_file_path)

    # Generate image
    #image_file = generate_image('image prompt')


if __name__ == "__main__":
    main()
