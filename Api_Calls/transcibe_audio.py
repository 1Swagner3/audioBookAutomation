import time
from google.cloud import speech, storage
import os

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
            print("Waiting for operation to complete...")
            time.sleep(10)

        response = operation.result()
    except Exception as e:
        print(f"Error during transcription: {e}")
        return

    # Prepare the output folder and file name
    output_folder = "Output_Audio_to_Text"
    os.makedirs(output_folder, exist_ok=True)
    base_name = os.path.basename(file_name)
    output_file_name = os.path.splitext(base_name)[0] + "_transcript.txt"
    output_file_path = os.path.join(output_folder, output_file_name)

    # Save the results to a file
    try:
        with open(output_file_path, "w") as text_file:
            if not response.results:
                print("No transcription results.")
            for result in response.results:
                transcript = result.alternatives[0].transcript
                print("Writing transcription to file...")
                text_file.write(transcript + "\n")
    except IOError as e:
        print(f"Error writing file: {e}")

    print(f"Transcription saved to {output_file_path}")

    return output_file_path
