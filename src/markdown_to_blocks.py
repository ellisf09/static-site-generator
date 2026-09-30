def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned = []
    for block in blocks:
        b = block.strip()
        if b:
            cleaned.append(b)
    return cleaned
