import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if re.match(r'^# .+', markdown):
        return BlockType.HEADING
    elif re.match(r'^```[\s\S]*```$', markdown, re.MULTILINE):
        return BlockType.CODE
    elif re.match(r'^> .+', markdown):
        return BlockType.QUOTE
    elif re.match(r'^- .+', markdown):
        return BlockType.UNORDERED_LIST
    elif re.match(r'^\d+\. .+', markdown):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH