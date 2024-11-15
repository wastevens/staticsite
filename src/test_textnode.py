import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "some url")
        node2 = TextNode("This is a text node", TextType.BOLD, "some url")
        self.assertEqual(node, node2)

    def test_neq_when_any_differences(self):
        node = TextNode("This is a text node", TextType.BOLD, "some url")
        self.assertNotEqual(node, TextNode("This is another text node", TextType.BOLD, "some url"))
        self.assertNotEqual(node, TextNode("This is a text node", TextType.ITALIC, "some url"))
        self.assertNotEqual(node, TextNode("This is a text node", TextType.BOLD, "another url"))

    def test_eq_with_optionals(self):
        self.assertEqual(TextNode(None, TextType.BOLD, "some url"), TextNode(None, TextType.BOLD, "some url"))
        self.assertEqual(TextNode("This is a text node", None, "some url"), TextNode("This is a text node", None, "some url"))
        self.assertEqual(TextNode("This is a text node", TextType.BOLD, None), TextNode("This is a text node", TextType.BOLD, None))
        self.assertEqual(TextNode("This is a text node", TextType.BOLD), TextNode("This is a text node", TextType.BOLD, None))
        self.assertEqual(TextNode("This is a text node"), TextNode("This is a text node", TextType.NORMAL))

if __name__ == "__main__":
    unittest.main()