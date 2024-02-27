import asyncio
from Api_Calls.transcibe_audio import transcribe_audio
from helper.text_to_speech import text_to_speech
from helper.improve_text import improve_text
from Api_Calls.dalle import generate_image


def main():
    
    # Get user input
    user_input = input("Please enter a google cloud storage: ")
    
    # Read audio file
    transcribed_text_file_path = transcribe_audio(user_input)

    # Process text
    improved_text_file_path = asyncio.run(improve_text(transcribed_text_file_path))
    
    # Convert processed text to speech
    text_to_speech(improved_text_file_path)

    # Generate image
    generate_image(improved_text_file_path)


if __name__ == "__main__":
    main()
