import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_blank_node(self):
        node1 = HTMLNode()
        self.assertIsNone(node1.tag)
        self.assertIsNone(node1.value)
        self.assertEqual(node1.children, [])
        self.assertEqual(node1.props, {})
    
    def test_node_with_tag_and_value(self):
        node1 = HTMLNode("h1", "Testing dss")
        self.assertEqual(node1.tag, "h1")
        self.assertEqual(node1.value, "Testing dss")
        self.assertEqual(node1.children, [])
        self.assertEqual(node1.props, {})

    def test_node_with_children(self):
        child = HTMLNode("p", "Child node")
        parent = HTMLNode("div", children=[child])
        self.assertEqual(parent.tag, "div")
        self.assertIsNone(parent.value)
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0].tag, "p")
        self.assertEqual(parent.children[0].value, "Child node")

    def test_node_with_props(self):
        node = HTMLNode("a", "Link", props={"href": "https://www.example.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Link")
        self.assertEqual(node.props, {"href": "https://www.example.com"})

if __name__ == "__main__":
    unittest.main()
