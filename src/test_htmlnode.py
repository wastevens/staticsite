import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        self.assertEqual('', HTMLNode(None, None, None, None).props_to_html())
        self.assertEqual(' ', HTMLNode(None, None, None, {}).props_to_html())
        self.assertEqual(' foo="bar"', HTMLNode(None, None, None, {"foo": "bar"}).props_to_html())
        self.assertEqual(' foo="bar" baz="baq"', HTMLNode(None, None, None, {"foo": "bar", "baz": "baq"}).props_to_html())

    def test_eq(self):
        self.assertEqual(HTMLNode(None, None, None, None), HTMLNode(None, None, None, None))
        self.assertEqual(HTMLNode("some tag", "some value", (HTMLNode(), HTMLNode()), {"foo":"bar", "baz":"baq"}), HTMLNode("some tag", "some value", (HTMLNode(), HTMLNode()), {"foo":"bar", "baz":"baq"}))

    def test_neq(self):
        self.assertNotEqual(HTMLNode("some tag", "some value", (HTMLNode()), {"foo":"bar"}), HTMLNode("another tag", "some value", (HTMLNode()), {"foo":"bar"}))
        self.assertNotEqual(HTMLNode("some tag", "some value", (HTMLNode()), {"foo":"bar"}), HTMLNode("some tag", "another value", (HTMLNode()), {"foo":"bar"}))
        self.assertNotEqual(HTMLNode("some tag", "some value", (HTMLNode()), {"foo":"bar"}), HTMLNode("some tag", "some value", (HTMLNode("a tag")), {"foo":"bar"}))
        self.assertNotEqual(HTMLNode("some tag", "some value", (HTMLNode()), {"foo":"bar"}), HTMLNode("some tag", "some value", (HTMLNode()), {"baz":"baq"}))


if __name__ == "__main__":
    unittest.main()