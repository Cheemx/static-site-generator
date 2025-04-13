import re

def extract_title(markdown):
    heading = re.findall(r"^#\s(.+)", markdown, re.MULTILINE)
    if not heading:
        raise Exception("Heading not found")
    return heading[0]