import asyncio
from utils.file_modes import MODE
from utils.file_saver import file_saver
from utils.split_text import split_text
from utils.combine_text_chunks import combine_chunks
from Api_Calls.chat_gpt_improve_text import get_improved_text

async def improve_text(file_path):
    
    print("Start improving text...")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text_chunks = split_text(text)

    # Create a list of coroutine objects for each text chunk
    print("Generate task list...")
    tasks = [get_improved_text(index, chunk) for index, chunk in enumerate(text_chunks)]

    # Process all tasks concurrently and wait for all to complete
    print("Process tasks...")
    improved_chunks = await asyncio.gather(*tasks)

    improved_text = combine_chunks(improved_chunks)
    
    # Create the output file name based on the input file name
    output_file_path = file_saver(file_path, improved_text, MODE.IMPROVE_TEXT)
    
    print("Text improved...")
    
    return output_file_path