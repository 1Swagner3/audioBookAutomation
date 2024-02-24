def split_text(text, max_length=1500):
    chunks = []
    current_chunk = ''

    for word in text.split():
        if len(current_chunk) + len(word) < max_length:
            current_chunk += word + ' '
        else:
            # Add the current chunk to the chunks list
            chunks.append(current_chunk)
            # Start a new chunk with the current word
            current_chunk = word + ' '

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)

    print("Chunks generated...", str(len(chunks)))
    return chunks
