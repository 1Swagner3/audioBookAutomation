from utils.file_modes import MODE
from utils.file_saver import file_saver
from utils.replace_names_in_text import replace_names_in_text

def replace_wrong_words(input_file_path):
    
    print("Start replacing wrong names...")

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except IOError as e:
        print(f"Error reading file {input_file_path}: {e}")
        return None

    # Split the text into smaller parts and replace wrong names
    optimized_text = replace_names_in_text(text)

    # Save the corrected text
    output_file_path = file_saver(input_file_path, optimized_text, MODE.CORRECTED)
    
    return output_file_path