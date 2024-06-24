from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_blank_node(self):
        with self.assertRaises(ValueError):
            LeafNode()

    def test_node_with_tag_and_value(self):
        node = LeafNode("h1", "Testing dss")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Testing dss")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

if __name__ == "__main__":
    unittest.main()