import re
# ![alt_text]() = \!\[(.*?)\]\((.*?)\)
# () = \((.*?)\)


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches



# def extract_markdown_images(text):
#     img_md = []
#     alt_texts = re.findall(r"\!\[(.*?)\]", text)
#     url = re.findall(r"\((.*?)\)", text)
#     if len(alt_texts) != len(url):
#         raise Exception("improper formatted markdown")
#     for i in range(len(alt_texts)):
#         img_md.append((alt_texts[i], url[i]))
#     return img_md

# def extract_markdown_links(text):
#     url_md = []
#     alt_texts = re.findall(r"\[(.*?)\]", text)
#     url = re.findall(r"\((.*?)\)", text)
#     if len(alt_texts) != len(url):
#         raise Exception("improper formatted markdown")
#     for i in range(len(alt_texts)):
#         url_md.append((alt_texts[i], url[i]))
#     return url_md