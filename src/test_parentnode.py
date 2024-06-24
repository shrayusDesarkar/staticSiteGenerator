import unittest
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_multiple_leaf_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "More normal text"),
            ]
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>Italic text</i>More normal text</p>"
        self.assertEqual(node.to_html(), expected_html)
    
    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Nested text")
                    ]
                ),
                LeafNode("span", "Span text")
            ]
        )
        expected_html = "<div><p>Nested text</p><span>Span text</span></div>"
        self.assertEqual(node.to_html(), expected_html)
    
    def test_children_with_no_tag(self):
        node = ParentNode(
            "div",
            [
                LeafNode(None, "Text without tag"),
                LeafNode("strong", "Strong text")
            ]
        )
        expected_html = "<div>Text without tag<strong>Strong text</strong></div>"
        self.assertEqual(node.to_html(), expected_html)
    
    def test_no_children_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div")
        self.assertTrue("Children requires a value" in str(context.exception))
    
    def test_no_tag_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("p", "Some text")])
        self.assertTrue("Tag requires a value" in str(context.exception))

if __name__ == '__main__':
    unittest.main()