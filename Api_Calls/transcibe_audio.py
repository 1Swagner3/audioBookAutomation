import threading
import time
from google.cloud import speech, storage
from utils.file_modes import MODE
from utils.file_saver import file_saver
from utils.spinning_cursor import spinning_cursor
from phraseHints import phrase_hints

def transcribe_audio(gcs_uri):
    
    # Initialize the client with the service account key
    client = speech.SpeechClient.from_service_account_json("optimum-harbor-413518-fd425d99bf79.json")

    print(f"Accessing file at: {gcs_uri}")

    # Check if the file exists in GCS
    storage_client = storage.Client()
    bucket_name, file_name = gcs_uri[5:].split('/', 1)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name) 
    if not blob.exists():
        print(f"File does not exist in GCS bucket: {gcs_uri}")
        return
    
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=44100,
        language_code="de-DE",
        enable_automatic_punctuation=True,
        use_enhanced=True,
        model='latest_long',
        speech_contexts=[speech.SpeechContext(phrases=phrase_hints)]
    )

    # Create a stop event for the spinner
    stop_event = threading.Event()

    # Start the spinner in a separate thread
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    spinner_thread.start()

    try:
        operation = client.long_running_recognize(config=config, audio=audio)
        print("Waiting for transcription operation to complete ... ", end="")

        while not operation.done():
            time.sleep(10)

        response = operation.result()
        print("\nTranscription completed successfully.")
    except Exception as e:
        print(f"\nError during transcription: {e}")
        return
    finally:
        # Stop the spinner
        stop_event.set()
        spinner_thread.join()

    # Prepare the output folder and file name
    output_file_path = file_saver(gcs_uri, response, MODE.TRANSCRIPTION)

    return output_file_path
