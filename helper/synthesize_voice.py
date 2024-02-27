import threading
from google.cloud import texttospeech

from helper.spinning_cursor import spinning_cursor

def synthesize_voice(text):
    # Initialize the client
    client = texttospeech.TextToSpeechClient.from_service_account_json("optimum-harbor-413518-fd425d99bf79.json")
    
    print("Synthesizing text...")
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3, 
        speaking_rate=1.0,
        pitch=0
        )

    ssml_text = f"<speak>{text}</speak>"
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)
    voice = texttospeech.VoiceSelectionParams(
        language_code='de-DE', 
        name='de-DE-Wavenet-D',
        ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
    
    
    # Create a stop event for the spinner
    stop_event = threading.Event()

    # Start the spinner in a separate thread
    spinner_thread = threading.Thread(target=spinning_cursor, args=(stop_event,))
    spinner_thread.start()

    try:
        response = client.synthesize_speech(
            input=synthesis_input, 
            voice=voice, 
            audio_config=audio_config
        )
        print("Waiting for text to speech operation to complete ... ", end="")
    except Exception as e:
        print(f"\nError during text synthesis: {e}")
        return None
    finally:
        # Stop the spinner
        stop_event.set()
        spinner_thread.join()
    
    return response.audio_content
