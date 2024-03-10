import asyncio
from Api_Calls.assembli_ai_transscription import transcribe_assembly_ai
from helper.replace_wrong_names import replace_wrong_words
from helper.text_to_speech import text_to_speech
from helper.improve_text import improve_text
from Api_Calls.dalle import generate_image


def main():
    
    # Get user input
    user_input = input("Please enter a local audio file path: ")
    
    # Get user input for the chapter number
    chapter_number = input("Please enter the chapter number: ")

    # Validate chapter number input (optional, but recommended)
    if not chapter_number.isdigit():
        print("Error: Chapter number should be numeric.")
        return
    
    # Read audio file
    transcribed_text_file_path = transcribe_assembly_ai(input_file_path=user_input, chapter_number=chapter_number)
    
    input("""
          Please review the transcribed file for any words that should be added to the replacement dictionary. 
          Press Enter to continue...
        """)
    
    corrected_text_file_path = replace_wrong_words(transcribed_text_file_path)

    # Process text
    improved_text_file_path = asyncio.run(improve_text(corrected_text_file_path))
    
    # Convert processed text to speech
    text_to_speech(improved_text_file_path)

    # Generate image
    generate_image(improved_text_file_path)


if __name__ == "__main__":
    main()
