def markdown_to_blocks(markdown):
    blocks =markdown.split('\n\n')
    for block in blocks:
        block.strip()
    return blocks