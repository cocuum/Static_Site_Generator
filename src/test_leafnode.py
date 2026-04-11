from leafnode import LeafNode

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
    