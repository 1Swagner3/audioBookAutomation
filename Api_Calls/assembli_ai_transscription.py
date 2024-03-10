import os
import threading
from dotenv import load_dotenv
import assemblyai
from utils.file_modes import MODE
from utils.file_saver import file_saver
from utils.spinning_cursor import spinning_cursor

def transcribe_assembly_ai(input_file_path, chapter_number):
    
    load_dotenv()
    api_key = os.environ.get("ASSEMBLI_AI_API_KEY")
    assemblyai.settings.api_key = api_key
    # Initialize the AssemblyAI transcriber with the API key
    transcriber = assemblyai.Transcriber()
    
    config = assemblyai.TranscriptionConfig(
        punctuate=True,
        format_text=True,
        language_code="de",   
    )
    
    # Create a stop event for the spinner
    stop_event = threading.Event()

    # Start the spinner in a separate thread
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    spinner_thread.start()

    transcript_text = None

    try:
        print("Submitting transcription request ... ")

        # Start the transcription process
        transcript = transcriber.transcribe(
            data=input_file_path, 
            config=config
            )
        
        # Checking if the transcription process has an attribute to get the result
        if hasattr(transcript, 'text'):
            transcript_text = transcript.text
            print("\nTranscription completed successfully.")
        else:
            print("\nTranscription process did not return text directly.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        # Stop the spinner
        stop_event.set()
        spinner_thread.join()
        
    output_file_path = file_saver("gs://audio_file_storage_v2/Chapter01-Read.mp3", transcript_text, MODE.TRANSCRIPTION, chapter_number)
    return output_file_path