import enum


class MODE(enum.Enum):
    TEXT_TO_SPEECH = "text_to_speech"
    IMPROVE_TEXT = "improve_text"
    TRANSCRIPTION = "transcription"

class FILE_UTILS:
    @staticmethod
    def get_output_folder(mode):
        folders = {
            MODE.TEXT_TO_SPEECH: "Output_Text_to_Speech",
            MODE.IMPROVE_TEXT: "Output_Improved_Text",
            MODE.TRANSCRIPTION: "Output_Audio_to_Text"
        }
        return folders.get(mode, None)

    @staticmethod
    def get_file_type(mode):
        file_types = {
            MODE.TEXT_TO_SPEECH: "mp3",
            MODE.IMPROVE_TEXT: "txt",
            MODE.TRANSCRIPTION: "txt"
        }
        return file_types.get(mode, None)

    @staticmethod
    def get_write_mode(mode):
        write_modes = {
            MODE.TEXT_TO_SPEECH: "wb",
            MODE.IMPROVE_TEXT: "w",
            MODE.TRANSCRIPTION: "w"
        }
        return write_modes.get(mode, None)
    
    @staticmethod
    def get_suffix(mode):
        suffixes = {
            MODE.TEXT_TO_SPEECH: "voice",
            MODE.IMPROVE_TEXT: "improved",
            MODE.TRANSCRIPTION: "transcript"
        }
        return suffixes.get(mode, None)
    
    @staticmethod
    def get_description_text(mode):
        descriptions = {
           MODE.TEXT_TO_SPEECH: "Voice",
           MODE.IMPROVE_TEXT: "Improved Text",
           MODE.TRANSCRIPTION: "Transcript"
       } 
        return descriptions.get(mode, None)