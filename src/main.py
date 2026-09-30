import os

import shutil
from generate_pages_recursive import generate_pages_recursive

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for name in os.listdir(src):
        src_path = os.path.join(src, name)
        dst_path = os.path.join(dst, name)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static(src_path, dst_path)

def main():
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
