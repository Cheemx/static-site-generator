import os

from md_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md_file_obj = open(from_path, mode='r')
    temp_file_obj = open(template_path, 'r')

    md_content = md_file_obj.read()
    temp_content = temp_file_obj.read()

    md_file_obj.close()
    temp_file_obj.close()

    md_content_html = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)  
    html_title_replace = temp_content.replace("{{ Title }}", title)
    new_html = html_title_replace.replace("{{ Content }}", md_content_html) 

    parent_dir = os.path.dirname(dest_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(new_html)