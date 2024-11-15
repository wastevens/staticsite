from enum import Enum

class NodeType(Enum):
    HTML = "html"
    LEAF = "leaf"
    TEXT = "text"

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type=TextType.NORMAL, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, o):
        if type(self) is not type(o):
            return False
        return self.text == o.text and self.text_type == o.text_type and self.url == o.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"