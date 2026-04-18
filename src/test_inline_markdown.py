import unittest
from markdown_inline import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_bold(self):
        nodes = TextNode("Hello **world**!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([nodes], "**", TextType.BOLD)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode("!", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_multi_bold(self):
        nodes = TextNode("This is **bolded** and **another bolded** text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([nodes], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("another bolded", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_italic(self):
        nodes = TextNode("This is _italic_ text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([nodes], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_multi_italic(self):
        nodes = TextNode("This is _italic-ed_ and _another italic-ed_ text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([nodes], "_", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic-ed", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("another italic-ed", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_code(self):
        nodes = TextNode("This is text with `code block` word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([nodes], "`", TextType.CODE)
        expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with ![image](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/fJRm4Vk.jpeg)"
            )
        self.assertListEqual(matches,
                            [
                                 ("image", "https://i.imgur.com/zjjcJKZ.png"),
                                 ("image2", "https://i.imgur.com/fJRm4Vk.jpeg"),
                            ]
                            )
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.test.com) and another [link2](https://www.test2.com)"
            )
        self.assertListEqual(matches,
                            [
                                ("link", "https://www.test.com"),
                                ("link2", "https://www.test2.com"),
                            ]
                            )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
            node = TextNode(
                "![image](https://www.example.COM/IMAGE.PNG)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
                ],
                new_nodes,
            )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.test.com) and another [link2](https://www.test2.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.test.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link2", TextType.LINK, "https://www.test2.com"
                ),
            ],
            new_nodes,
        )

    def test_split_link_single(self):
            node = TextNode(
                "[link](https://www.test.com)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("link", TextType.LINK, "https://www.test.com"),
                ],
                new_nodes,
            )

    def test_text_to_textnodes(self):
        result = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()