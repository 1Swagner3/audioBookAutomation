from google.cloud import speech
import io
import os

def transcribe_audio(speech_file, language_code="de-DE"):
    # Initialize the client with the service account key
    client = speech.SpeechClient.from_service_account_json("../optimum-harbor-413518-fd425d99bf79.json")

    # Read the audio file
    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    # Transcribe the audio file
    response = client.recognize(config=config, audio=audio)

    # Prepare the output folder and file name
    output_folder = "../Output_Audio_to_Text"
    os.makedirs(output_folder, exist_ok=True)
    base_name = os.path.basename(speech_file)
    output_file_name = os.path.splitext(base_name)[0] + "_transcript.txt"
    output_file_path = os.path.join(output_folder, output_file_name)

    # Save the results to a file
    with open(output_file_path, "w") as text_file:
        for result in response.results:
            text_file.write(result.alternatives[0].transcript + "\n")

    print(f"Transcription saved to {output_file_path}")

    return output_file_path