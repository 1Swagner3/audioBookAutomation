from helper.file_modes import MODE, FILE_UTILS
import os
from urllib.parse import urlparse


def file_saver(input_file_path, input, mode):
    print("Saving file...")
    
    base_name = extract_file_name(input_file_path, mode)
    chapter_number = base_name[7:9]
    output_file_name = f"Chapter{chapter_number}_{FILE_UTILS.get_suffix(mode)}.{FILE_UTILS.get_file_type(mode)}"
    output_folder = FILE_UTILS.get_output_folder(mode)
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, output_file_name)
    
    if mode == MODE.TRANSCRIPTION:
        with open(output_file_path, FILE_UTILS.get_write_mode(mode)) as text_file:
            for result in input.results:
                transcript = result.alternatives[0].transcript
                text_file.write(transcript + "\n")
    else:
        with open(output_file_path, FILE_UTILS.get_write_mode(mode)) as out:
            out.write(input)
    
    print(f"{FILE_UTILS.get_description_text(mode)} file saved to to {output_file_path}")
    return output_file_path

def extract_file_name(file_path, mode):
    if mode == MODE.TRANSCRIPTION and file_path.startswith('gs://'):
        parsed_uri = urlparse(file_path)
        return os.path.basename(parsed_uri.path)
    else:
        return os.path.basename(file_path)