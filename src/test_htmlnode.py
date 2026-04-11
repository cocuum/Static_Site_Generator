import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(
            parent.tag,
            "p",
        )
        self.assertEqual(
            parent.value,
            "This is a paragraph",
        )
        self.assertEqual(
            parent.children,
            [child],
        )
        self.assertEqual(
            parent.props,
            None,
        )

    def test_props_to_html(self):
        node = HTMLNode(
            "a", 
            "Click here",
            None,
            {"class": "btn", "href": "https://www.test.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="btn" href="https://www.test.com"',
        )
    
    def test_repr(self):
        node = HTMLNode(
            "h1",
            "This is a paragraph heading",
            None,
            {"class": "title"},
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(h1, This is a paragraph heading, children: None, {'class': 'title'})",
        )

    def test_has_children(self):
        child1 = HTMLNode(
            "a",
            "WA City1",
            None,
            {"href": "https://www.city1.com"},
        )
        child2 = HTMLNode(
            "a",
            "WA City2",
            None,
            {"href": "https://www.city2.com"},
        )
        child3 = HTMLNode(
            "a",
            "WA City3",
            None,
            {"href": "https://www.city3.com"},
        )
        parent = HTMLNode(
            "ul",
            None,
            [child1, child2, child3],
            None,
        )
        self.assertEqual(
            parent.children,
            [child1, child2, child3],
        )

    def test_leaf_to_html_p(self):
        node = LeafNode(
            "p",
            "Hello, world!",
        )
        self.assertEqual(
            node.to_html(),
            "<p>Hello, world!</p>",
        )

    def test_leaf_to_html_has_props(self):
        node = LeafNode(
            "span",
            "Hello, world!",
            {"class": "highlight"},
        )
        self.assertEqual(
            node.to_html(),
            '<span class="highlight">Hello, world!</span>',
        )

    def test_leaf_repr(self):
        node = LeafNode(
            "p",
            "This is a paragraph",
            {"class": "title"},
        )
        self.assertEqual(
            repr(node),
            "LeafNode(p, This is a paragraph, {'class': 'title'})",
        )

    def test_leaf_missing_value(self):
        leaf = LeafNode(
            "h2",
            None,
        )
        with self.assertRaises(ValueError) as c:
            leaf.to_html()
        self.assertEqual(
            str(c.exception),
            "invalid HTML: LeafNode must have a value",
        )
    
    def test_missing_tag(self):
        leaf = LeafNode(
            None,
            "Hello, world!",
        )
        parent = ParentNode(
            None,
            [leaf],
        )
        self.assertEqual(
            leaf.to_html(),
            "Hello, world!",
        )
        with self.assertRaises(ValueError) as c:
            parent.to_html()
        self.assertEqual(
            str(c.exception),
            "invalid HTML: ParentNode must have a tag",
        )
    
    def test_to_html_with_children(self):
        child_node = LeafNode(
            "span",
            "child",
        )
        parent_node = ParentNode(
            "div",
            [child_node],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(
            "b",
            "grandchild",
        )
        child_node = ParentNode(
            "span",
            [grandchild_node],
        )
        parent_node = ParentNode(
            "div",
            [child_node],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_parent_missing_children(self):
        parent = ParentNode(
            "div",
            None,
            {"class": "container", "id": "specials"},
        )
        with self.assertRaises(ValueError) as c:
            parent.to_html()
        self.assertEqual(
            str(c.exception),
            "invalid HTML: ParentNode must have children",
        )
    
    def test_parent_has_multiple_children(self):
        leaf1 = LeafNode(
            "li",
            "WA City1",
            {"href": "https://www.city1.com"},
        )
        leaf2 = LeafNode(
            "li",
            "WA City2",
            {"href": "https://www.city2.com"},
        )
        leaf3 = LeafNode(
            "li",
            "WA City3",
            {"href": "https://www.city3.com"},
        )
        parent = ParentNode(
            "ol",
            [leaf1, leaf2, leaf3],
            {"class": "city-list"},
        )
        self.assertEqual(
            parent.to_html(),
            '<ol class="city-list"><li href="https://www.city1.com">WA City1</li><li href="https://www.city2.com">WA City2</li><li href="https://www.city3.com">WA City3</li></ol>',
        )
    
    def test_parent_repr(self):
        child_node = LeafNode(
            "span",
            "child",
        )
        parent_node = ParentNode(
            "div",
            [child_node],
        )
        self.assertEqual(
            repr(parent_node),
            "ParentNode(div, children: [LeafNode(span, child, None)], None)",
        )

if __name__ == "__main__":
    unittest.main()