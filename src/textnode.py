from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        if text_type not in TextType:
            raise ValueError(f"Invalid TextType: {text_type}")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False

        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
                )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception(f"Invalid TextType:{text_node.text_type}")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {
                "href": text_node.url
            })
        case TextType.IMAGE:
            return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text
            })
        case _:
            raise Exception(f"Invalid TextType: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_list = node.text.split(delimiter)
        if len(text_list) % 2 == 0:
            raise ValueError("invalid markdown")
        for i, text in enumerate(text_list):
            if text == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))  
    return new_nodes