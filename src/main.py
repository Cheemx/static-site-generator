import shutil

from static_to_public import static_to_public
print("hello world")
from generate_page import generate_pages_recursive

def main():
    shutil.rmtree("public")
    static_to_public("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()