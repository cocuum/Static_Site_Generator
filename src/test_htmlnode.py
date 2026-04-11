import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        child = HTMLNode(
            "span",
            "This is a highlighted text in the paragraph",
            None,
            {"style": "background-color:yellow"}
        )
        parent = HTMLNode(
            "p",
            "This is a paragraph",
            [child],
            None
        )
        self.assertEqual(parent.tag, "p")
        self.assertEqual(parent.value, "This is a paragraph")
        self.assertEqual(parent.children, [child])
        self.assertEqual(parent.props, None)

    def test_props_to_html(self):
        node = HTMLNode("a", "Click here", None, {"href": "https://www.test.com"})
        self.assertEqual(node.props_to_html(), " href=https://www.test.com")
    
    def test_repr(self):
        node = HTMLNode("h1", "This is a paragraph heading")
        self.assertEqual(repr(node), "HTMLNode(h1, This is a paragraph heading, None, None)")

    def test_has_children(self):
        child1 = HTMLNode("a", "WA City1", None, {"href": "https://www.city1.com"})
        child2 = HTMLNode("a", "WA City2", None, {"href": "https://www.city2.com"})
        child3 = HTMLNode("a", "WA City3", None, {"href": "https://www.city3.com"})
        parent = HTMLNode("ul", None, [child1, child2, child3], None)
        self.assertEqual(parent.children, [child1, child2, child3])