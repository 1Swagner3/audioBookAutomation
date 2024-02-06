from google.cloud import texttospeech
import os

def text_to_speech(input_file_path, language_code='de-DE', voice_name='de-DE-Standard-A', speaking_rate=1.0):
    # Initialize the client with the service account key
    client = texttospeech.TextToSpeechClient.from_service_account_json("../optimum-harbor-413518-fd425d99bf79.json")

    # Read the text from the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code and the ssml voice gender
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name
    )

    # Select the type of audio file you want
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate
    )

    # Perform the text-to-speech request
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    
    # Prepare the output file name and path
    base_name = os.path.basename(input_file_path)
    output_folder = "../Output_Text_to_Speech"
    output_file_name = os.path.splitext(base_name)[0].replace("_transcript", "") + "_audio.mp3"
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, output_file_name)

    # Write the audio content to the file
    with open(output_file_path, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_file_path}"')

    return output_file_path
