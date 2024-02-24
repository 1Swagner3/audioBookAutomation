import time
from google.cloud import speech, storage
import os
from helper.file_modes import MODE

from helper.file_saver import file_saver

def transcribe_audio(gcs_uri, language_code="de-DE"):
    
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
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    # Asynchronously transcribe the audio file
    try:
        operation = client.long_running_recognize(config=config, audio=audio)
        while not operation.done():
            print("Waiting for transcription operation to complete...")
            time.sleep(10)

        response = operation.result()
    except Exception as e:
        print(f"Error during transcription: {e}")
        return

    # Prepare the output folder and file name
    output_file_path = file_saver(gcs_uri, response, MODE.TRANSCRIPTION)

    return output_file_path
