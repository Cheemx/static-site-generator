from textnode import TextNode
from textnode import TextType
print("hello world")

def main():
    tn_obj = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn_obj)


main()
