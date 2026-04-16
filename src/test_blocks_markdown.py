import unittest
from blocks_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type,
)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
            heading_bl = "# heading1\n\n## heading2\n\n### heading3\n\n#### heading4\n\n##### heading5\n\n###### heading6"
            result1 = block_to_block_type(heading_bl)
            self.assertEqual(result1, BlockType.HEADING)

            code_bl = "```\nRegExr was created by gskinner.com.\n```"
            result2 = block_to_block_type(code_bl)
            self.assertEqual(result2, BlockType.CODE)

            quote_bl = "> RegExr was created by gskinner.com. Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode."
            result3 = block_to_block_type(quote_bl)
            self.assertEqual(result3, BlockType.QUOTE)

            unordered_bl = "- RegExr was created by gskinner.com. Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode.\n- The side bar includes a Cheatsheet, full Reference, and Help.You can also Save & Share with the Community and view patterns you create or favorite in My Patterns.\n- Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English."
            result4 = block_to_block_type(unordered_bl)
            self.assertEqual(result4, BlockType.ULIST)

            ordered_bl = "1. RegExr was created by gskinner.com.\n2. The side bar includes a Cheatsheet, full Reference, and Help.\n3. Explore results with the Tools below."
            result5 = block_to_block_type(ordered_bl)
            self.assertEqual(result5, BlockType.OLIST)

if __name__ == "__main__":
    unittest.main()