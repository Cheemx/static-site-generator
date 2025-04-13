from markdown_to_blocks import markdown_to_blocks
from text_to_textnode import text_to_textnodes
from textnode import text_node_to_html_node
from blocknode import block_to_block_type, BlockType
from htmlnode import ParentNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.PARAGRAPH:
                p_node = ParentNode("p", text_to_children(block))
                children.append(p_node)
            case BlockType.HEADING:
                head_cnt = block.count("#", 0, 7)
                h_node = ParentNode(f"h{head_cnt}", text_to_children(block.lstrip('# ')))
                children.append(h_node)
            case BlockType.QUOTE:
                q_node = ParentNode("blockquote", text_to_children(block.lstrip("> ")))
                children.append(q_node)
            case BlockType.UNORDERED_LIST:
                ul_node = ParentNode("ul",  list_to_list_node(block))
                children.append(ul_node)
            case BlockType.ORDERED_LIST:
                ol_node = ParentNode("ol",  list_to_list_node(block))
                children.append(ol_node)
            case BlockType.CODE:
                code_nodes = block_to_code_node(block)
                code_parent = ParentNode("code", code_nodes)
                pre_node = ParentNode("pre", [code_parent])
                children.append(pre_node)
    div_node = ParentNode("div", children)
    return div_node

def text_to_children(text):
    normalized_text = ' '.join(text.split())
    node_list = []
    text_nodes = text_to_textnodes(normalized_text)
    for node in text_nodes:
        node_list.append(text_node_to_html_node(node))
    return node_list

def list_to_list_node(text):
    lines = text.split('\n')  # Split the text into lines
    list_nodes = []
    for line in lines:
        if line.strip():  # Process non-empty lines only
            if line.lstrip().startswith('- '):  # Handle unordered list
                content = line.lstrip()[2:].strip()  # Remove '- ' and extra spaces
            elif line.lstrip().startswith(tuple(f"{i}. " for i in range(1, 101))):  # Ordered list
                # Remove the number and trailing ". " (e.g., "1. Gandalf" -> "Gandalf")
                content = line.lstrip().split('. ', 1)[1].strip()
            else:  # Fallback for unexpected lines
                content = line.strip()
            
            # Print for debugging:
            print(f"Processed content: {content}")

            # Create a <li> node for each item and pass to text_to_children
            list_nodes.append(ParentNode("li", text_to_children(content)))

    return list_nodes

def block_to_code_node(text):
    # For triple backtick code blocks
    if text.startswith("```") and text.endswith("```"):
        # Remove the opening and closing ``` lines
        lines = text.split('\n')
        if len(lines) >= 2:
            # Process lines between backticks
            content_lines = lines[1:-1]
            
            # Check for common indentation
            min_indent = float('inf')
            for line in content_lines:
                if line.strip():  # Skip empty lines
                    indent = len(line) - len(line.lstrip())
                    min_indent = min(min_indent, indent)
            
            # Remove common indentation
            if min_indent < float('inf'):
                content_lines = [line[min_indent:] if line.strip() else line for line in content_lines]
            
            # Add the newline at the end of the content
            code_content = '\n'.join(content_lines) + '\n'
        else:
            code_content = ""
    else:
        # For indented code blocks
        code_content = text
    
    from textnode import TextNode, TextType
    text_node = TextNode(code_content, TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    
    return [html_node]