import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dst_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok=True)
            generate_pages_recursive(src_path, template_path, dst_path, basepath)

        elif entry.endswith(".md"):
            html_name = entry.replace(".md", ".html")
            final_dst = os.path.join(dest_dir_path, html_name)
            generate_page(src_path, template_path, final_dst, basepath)
