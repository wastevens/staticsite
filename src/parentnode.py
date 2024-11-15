from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Must have tag")
        if self.children == None:
            raise ValueError("Must have zero or more children")
        s = ""
        s += f"<{self.tag}{self.props_to_html()}>"
        for c in self.children:
            s += c.to_html()
        s += f"</{self.tag}>"
        return s
    
    def __eq__(self, o):
        if type(self) is not type(o):
            return False
        return self.tag == o.tag and self.children == o.children and self.props == o.props
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
