import unittest
from inline_markdown import split_nodes_delimiter
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

if __name__ == "__name__":
    unittest.main()