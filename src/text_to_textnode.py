from split_img_and_links import split_nodes_image, split_nodes_link
from textnode import *

def text_to_textnodes(text):
    old_node = TextNode(text, TextType.TEXT)
    img_nodes = split_nodes_image([old_node])
    link_nodes = split_nodes_link(img_nodes)
    bold_nodes = split_nodes_delimiter(link_nodes, "**", TextType.BOLD)
    code_nodes = split_nodes_delimiter(bold_nodes,"`", TextType.CODE)
    italic_nodes = split_nodes_delimiter(code_nodes, "_", TextType.ITALIC)
    return italic_nodes