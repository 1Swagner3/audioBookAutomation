import os
import re
from urllib.parse import urlparse
from io import BytesIO
import requests
from PIL import Image

from utils.file_modes import MODE, FILE_UTILS

def file_saver(input_file_path, input, mode, chapter_number=None):
    print("""
          -----------------------------------------------------
          Saving file...
          """)

    if chapter_number is None:
        # Extract chapter number from file path if not provided
        match = re.search(r"Chapter(\d+)", input_file_path)
        if match:
            chapter_number = match.group(1)
        else:
            print("Error: Chapter number not found in the file path.")
            return

    output_file_name = f"Chapter{chapter_number}_{FILE_UTILS.get_suffix(mode)}.{FILE_UTILS.get_file_type(mode)}"
    output_folder = FILE_UTILS.get_output_folder(mode)
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, output_file_name)

    if mode == MODE.TEXT_TO_SPEECH:
        # Exporting the AudioSegment object to a file
        input.export(output_file_path, format=FILE_UTILS.get_file_type(mode))
    elif mode == MODE.IMAGE:
        # Handle image saving
        image_url = input
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        image.save(output_file_path)
    else:
        with open(output_file_path, 'w') as out:
            out.write(input)
    
    print(f"""
          {FILE_UTILS.get_description_text(mode)} file saved to {output_file_path}
          -----------------------------------------------------
          """)
    return output_file_path
