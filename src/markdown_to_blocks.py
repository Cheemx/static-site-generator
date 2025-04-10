import re

def markdown_to_blocks(markdown):
    # Strip the entire markdown document
    markdown = markdown.strip()
    
    # Split by one or more blank lines
    blocks = re.split(r'\n\s*\n', markdown)
    
    processed_blocks = []
    for block in blocks:
        if block:
            # Don't modify code blocks with triple backticks
            if block.startswith("```") and block.endswith("```"):
                processed_blocks.append(block)
            else:
                # For indented code blocks
                lines = block.split('\n')
                if all(line.startswith('    ') for line in lines if line):
                    lines = [line[4:] for line in lines]  
                processed_blocks.append('\n'.join(lines))
    
    return processed_blocks