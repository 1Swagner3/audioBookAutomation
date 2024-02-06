import split_text
import combine_text_chunks
from Api_Calls import chat_gpt
import os

def improve_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    text_chunks = split_text(text)
    
    improved_chunks = [chat_gpt.get_improved_text(chunk) for chunk in text_chunks]
    
    improved_text = combine_text_chunks(improved_chunks)
    
    # Create the output file name based on the input file name
    base_name = os.path.basename(file_path)
    output_file_name = os.path.splitext(base_name)[0] + "_improved.txt"
    output_folder = "../Output_Improved_Text"
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(improved_text)

    return output_file_path