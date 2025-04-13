import shutil

from static_to_public import static_to_public
print("hello world")
from generate_page import generate_page

def main():
    shutil.rmtree("public")
    static_to_public("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()