from htmlnode import HTMLNode
from inline_markdown import extract_title
from block_markdown import markdown_to_html_node
import os
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path) as f:
        from_path_data = f.read()
    with open(template_path) as f:
        template_path_data = f.read()

    html = markdown_to_html_node(from_path_data).to_html()
    title = extract_title(from_path_data)
    template = template_path_data.replace("{{ Title }}", title).replace("{{ Content }}", html)
    dest_name = os.path.dirname(dest_path)
    os.makedirs(dest_name, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
