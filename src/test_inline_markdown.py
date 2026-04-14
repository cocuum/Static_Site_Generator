import unittest
from inline_markdown import (split_nodes_delimiter,
                             extract_markdown_images,
                             extract_markdown_links,
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
            "This is text with [link](https://www.test.com) and [link2](https://www.test2.com)"
            )
        self.assertListEqual(matches,
                            [
                                ("link", "https://www.test.com"),
                                ("link2", "https://www.test2.com"),
                            ]
                            )


if __name__ == "__name__":
    unittest.main()