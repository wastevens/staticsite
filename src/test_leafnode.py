import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(LeafNode(None, None, None), LeafNode(None, None, None))
        self.assertEqual(LeafNode("some tag", "some value", {"foo":"bar", "baz":"baq"}), LeafNode("some tag", "some value", {"foo":"bar", "baz":"baq"}))

    def test_neq(self):
        self.assertNotEqual(LeafNode("some tag", "some value", {"foo":"bar"}), LeafNode("another tag", "some value", {"foo":"bar"}))
        self.assertNotEqual(LeafNode("some tag", "some value", {"foo":"bar"}), LeafNode("some tag", "another value", {"foo":"bar"}))
        self.assertNotEqual(LeafNode("some tag", "some value", {"foo":"bar"}), LeafNode("some tag", "some value", {"baz":"baq"}))

    def test_to_html(self):
        self.assertEqual('<a foo="bar" baz="baq">some value</a>', LeafNode("a", "some value", {"foo":"bar", "baz":"baq"}).to_html())
        self.assertEqual('some value', LeafNode(None, "some value").to_html())

if __name__ == "__main__":
    unittest.main()