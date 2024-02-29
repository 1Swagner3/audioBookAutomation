import re
from utils.replacement_dict import replacement_dict

def replace_names_in_text(text):
    def replace_match(match):
        incorrect_name = match.group(0)
        for correct, incorrects in replacement_dict.items():
            if incorrect_name in incorrects:
                return correct
        return incorrect_name

    all_incorrect_names = [re.escape(name) for incorrects in replacement_dict.values() for name in incorrects]
    pattern = r'\b(?:' + '|'.join(all_incorrect_names) + r')\b'
    corrected_text = re.sub(pattern, replace_match, text, flags=re.IGNORECASE)

    return corrected_text