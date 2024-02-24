import asyncio
from Api_Calls.transcibe_audio import transcribe_audio
from Api_Calls.text_to_speech import text_to_speech
from Api_Calls.chat_gpt import get_improved_text
from Api_Calls import text_to_speech
from helper.improve_text import improve_text


def main():
    
    # Get user input
    #user_input = input("Please enter a google cloud storage: ")
    
    # Read audio file
    #transcribed_text_file_path = transcribe_audio(user_input)

    # Process text
    improved_text_file_path = asyncio.run(improve_text('Output_Audio_to_Text/Chapter01-Read_transcript.txt'))
    # Convert processed text to speech
    #speech_file = text_to_speech(processed_text)

    # Generate image
    #image_file = generate_image('image prompt')


if __name__ == "__main__":
    main()
