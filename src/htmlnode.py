class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        return " " + " ".join(map(lambda t: f"{t[0]}=\"{t[1]}\"", self.props.items()))
    
    def __eq__(self, o):
        if type(self) is not type(o):
            return False
        return self.tag == o.tag and self.value == o.value and self.children == o.children and self.props == o.props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
