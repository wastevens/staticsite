from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, (), props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Must have value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __eq__(self, o):
        if type(self) is not type(o):
            return False
        return self.tag == o.tag and self.value == o.value and self.children == o.children and self.props == o.props
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
