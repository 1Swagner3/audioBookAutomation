def split_text(text, max_length=1000):
    # Splits text into chunks of max_length, on sentence/paragraph boundaries.
    sentences = text.split('. ')
    chunks = []
    current_chunk = ''

    for sentence in sentences:
        if len(current_chunk) + len(sentence) > max_length:
            chunks.append(current_chunk)
            current_chunk = sentence
        else:
            current_chunk += sentence + '. '
    chunks.append(current_chunk)  # Add the last chunk
    return chunks