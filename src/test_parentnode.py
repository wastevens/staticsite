import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(ParentNode(None, None, None), ParentNode(None, None, None))
        self.assertEqual(ParentNode("some tag", (HTMLNode(), HTMLNode()), {"foo":"bar", "baz":"baq"}), ParentNode("some tag", (HTMLNode(), HTMLNode()), {"foo":"bar", "baz":"baq"}))

    def test_neq(self):
        self.assertNotEqual(ParentNode("some tag", (HTMLNode()), {"foo":"bar"}), ParentNode("another tag", (HTMLNode()), {"foo":"bar"}))
        self.assertNotEqual(ParentNode("some tag", (HTMLNode()), {"foo":"bar"}), ParentNode("some tag", (HTMLNode(), HTMLNode()), {"foo":"bar"}))
        self.assertNotEqual(ParentNode("some tag", (HTMLNode()), {"foo":"bar"}), ParentNode("some tag", (HTMLNode()), {"baz":"baq"}))

    def test_to_html(self):
        self.assertEqual('<p></p>', ParentNode("p", ()).to_html())
        pass
        #self.assertEqual('<a foo="bar" baz="baq">some value</a>', LeafNode("a", "some value", {"foo":"bar", "baz":"baq"}).to_html())
        #self.assertEqual('some value', LeafNode(None, "some value").to_html())

if __name__ == "__main__":
    unittest.main()