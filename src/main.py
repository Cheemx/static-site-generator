import shutil
import sys

from static_to_public import static_to_public
print("hello world")
from generate_page import generate_pages_recursive

def main():
    # shutil.rmtree("public")
    basepath = "/" if len(sys.argv) < 2 else sys.argv[1]
    static_to_public("static", "docs")
    generate_pages_recursive(basepath, "template.html", "content", "docs")

main()