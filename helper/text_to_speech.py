import threading
from Api_Calls.elevenLabs_text_to_speech import elevenLabs_text_to_speech
from utils.spinning_cursor import spinning_cursor
from utils.split_text import split_text
from utils.file_saver import file_saver
from utils.file_modes import MODE
from pydub import AudioSegment

def text_to_speech(input_file_path):
    print("Start text to speech...")

    # Start the spinner in a separate thread
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    spinner_thread.start()

    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into smaller parts
    chunks = split_text(text, max_length=2000)
    
    # Initialize a list to hold audio segments
    audio_segments = []

    # Convert each chunk to audio
    for index, chunk in enumerate(chunks):
        try:
            audio_segment = elevenLabs_text_to_speech(text=chunk, index=index)
            audio_segments.append(audio_segment)
        except Exception as e:
            print(f"Error processing chunk: {e}")
            continue

    # Stop the spinner once all chunks are processed
    stop_event.set()
    spinner_thread.join()

    # Combine all audio segments
    print("Combining audio segments...")
    combined_audio = AudioSegment.empty()
    for segment in audio_segments:
        combined_audio += segment

    # Use file_saver to save the combined audio
    output_file_path = file_saver(input_file_path, combined_audio, MODE.TEXT_TO_SPEECH)

    print("\nText to Speech done...")
    return output_file_path
