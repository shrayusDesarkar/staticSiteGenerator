import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):    
    def test_different_text_content(self):
        node1 = TextNode("Hello, world!", "bold", "url1")
        node2 = TextNode("Greetings, everyone!", "bold", "url1")
        self.assertNotEqual(node1, node2)

    def test_different_text_type(self):
        node1 = TextNode("This is a text node", "bold", "url1")
        node2 = TextNode("This is a text node", "italic", "url1")
        self.assertNotEqual(node1, node2)

    def test_different_url(self):
        node1 = TextNode("This is a text node", "bold", "url1")
        node2 = TextNode("This is a text node", "bold", "url2")
        self.assertNotEqual(node1, node2)

    def test_equal_nodes(self):
        node1 = TextNode("Hello, world!", "italic", "url1")
        node2 = TextNode("Hello, world!", "italic", "url1")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()