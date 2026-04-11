import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_html_node(self):
        child = HTMLNode(
            "span",
            "This is a highlighted text in the paragraph",
            None,
            {"style": "background-color:yellow"},
        )
        parent = HTMLNode(
            "p",
            "This is a paragraph",
            [child],
            None,
        )
        self.assertEqual(parent.tag, "p")
        self.assertEqual(parent.value, "This is a paragraph")
        self.assertEqual(parent.children, [child])
        self.assertEqual(parent.props, None)

    def test_props_to_html(self):
        node = HTMLNode(
            "a", 
            "Click here",
            None,
            {"class": "btn", "href": "https://www.test.com"},
        )
        self.assertEqual(node.props_to_html(), ' class="btn" href="https://www.test.com"')
    
    def test_repr(self):
        node = HTMLNode(
            "h1",
            "This is a paragraph heading",
            None,
            {"class": "title"},
        )
        self.assertEqual(repr(node), "HTMLNode(h1, This is a paragraph heading, children: None, {'class': 'title'})")

    def test_has_children(self):
        child1 = HTMLNode("a", "WA City1", None, {"href": "https://www.city1.com"})
        child2 = HTMLNode("a", "WA City2", None, {"href": "https://www.city2.com"})
        child3 = HTMLNode("a", "WA City3", None, {"href": "https://www.city3.com"})
        parent = HTMLNode("ul", None, [child1, child2, child3], None)
        self.assertEqual(parent.children, [child1, child2, child3])

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_has_props(self):
        node = LeafNode("span", "Hello, world!", {"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Hello, world!</span>')

    def test_leaf_repr(self):
        node = LeafNode(
                "p",
                "This is a paragraph",
                {"class": "title"},
            )
        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph, {'class': 'title'})")
    
if __name__ == "__main__":
    unittest.main()