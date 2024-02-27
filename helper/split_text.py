import re

def split_text(text, max_length=1500):
    # Use a regular expression to split text at sentence boundaries
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ''

    for sentence in sentences:
        # Check if adding the sentence would exceed the max length
        if len(current_chunk + sentence) <= max_length:
            current_chunk += sentence + ' '
        else:
            # If the current chunk is too long, start a new chunk
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = sentence + ' '

    if current_chunk:
        chunks.append(current_chunk.strip())

    print("Chunks generated:", len(chunks))
    return chunks


