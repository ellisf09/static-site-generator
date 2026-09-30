from blocktype import BlockType

def block_to_block_type(block):
    if block.startswith("#"):
        hashes = 0
        for c in block:
            if c == "#":
                hashes += 1
            else:
                break
        if 1 <= hashes <= 6 and block[hashes:hashes+1] == " ":
            return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered = True
    for i, line in enumerate(lines, start=1):
        prefix = f"{i}. "
        if not line.startswith(prefix):
            ordered = False
            break
    if ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
