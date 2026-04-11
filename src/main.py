from textnode import TextNode, TextType


def main():
    node = TextNode("The Silent Whale", TextType.LINK, "https://www.silentwhale.com")
    print(node)


main()
