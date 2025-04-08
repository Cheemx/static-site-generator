from textnode import TextNode, TextType
from md_extraction import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for match in matches:
            image_alt = match[0]
            image_link = match[1]
            sections = current_text.split(f"![{image_alt}]({image_link})", 1)
            if len(sections) != 2:
                raise ValueError("invlaid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""
            
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        if len(matches) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for match in matches:
            url_text = match[0]
            url = match[1]
            sections = current_text.split(f"[{url_text}]({url})", 1)
            if len(sections) != 2:
                raise ValueError("invlaid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(url_text, TextType.LINK, url))
            if len(sections) > 1:
                current_text = sections[1]
            else:
                current_text = ""
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes