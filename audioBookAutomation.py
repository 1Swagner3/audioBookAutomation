from Api_Calls.transcibe_audio import transcribe_audio
from Api_Calls import text_to_speech


def main():
    
    # Get user input
    user_input = input("Please enter a google cloud storage: ")
    
    # Read audio file
    transcribed_text = transcribe_audio(user_input)

    # Process text
    #processed_text = text_to_speech(transcribed_text)

    # Convert processed text to speech
    #speech_file = text_to_speech(processed_text)

    # Generate image
    #image_file = generate_image('image prompt')


if __name__ == "__main__":
    main()
