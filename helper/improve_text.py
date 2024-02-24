import asyncio
from helper.split_text import split_text
from helper.combine_text_chunks import combine_chunks
from Api_Calls.chat_gpt import get_improved_text
import os

async def improve_text(file_path):
    
    print("Start improving text...")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text_chunks = split_text(text)

    # Create a list of coroutine objects for each text chunk
    print("Generate task list...")
    tasks = [get_improved_text(chunk) for chunk in text_chunks]

    # Process all tasks concurrently and wait for all to complete
    print("Process tasks...")
    improved_chunks = await asyncio.gather(*tasks)

    improved_text = combine_chunks(improved_chunks)
    
    # Create the output file name based on the input file name
    base_name = os.path.basename(file_path)
    output_file_name = os.path.splitext(base_name)[0] + "_improved.txt"
    output_folder = "Output_Improved_Text"
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(improved_text)

    print(f"Improved text saved to {output_file_path}")
    return output_file_path