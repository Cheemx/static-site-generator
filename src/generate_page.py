import os
import pathlib

from md_to_html import markdown_to_html_node
from extract_title import extract_title

def generate_page(basepath, template_path, content_path, dest_path):

    md_file_obj = open(content_path, mode='r')
    temp_file_obj = open(template_path, 'r')

    md_content = md_file_obj.read()
    temp_content = temp_file_obj.read()

    md_file_obj.close()
    temp_file_obj.close()

    md_content_html = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)  
    html_title_replace = temp_content.replace("{{ Title }}", title)
    html_content_replace = html_title_replace.replace("{{ Content }}", md_content_html)

    html_href_replace = html_content_replace.replace("href=\"/", f"href=\"{basepath}") 

    new_html = html_href_replace.replace("src=\"/", f"src=\"{basepath}") 

    parent_dir = os.path.dirname(dest_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(new_html)

def generate_pages_recursive(basepath, template_path, dir_path_content, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path) and entry_path.endswith('.md'):
            rel_path = os.path.relpath(entry_path, dir_path_content)
            dest_path = os.path.join(dest_dir_path, rel_path.replace('.md', '.html'))
            generate_page(basepath, template_path, entry_path, dest_path)

        elif os.path.isdir(entry_path):
            new_dest_dir = os.path.join(dest_dir_path, entry)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(basepath, template_path, entry_path, new_dest_dir)