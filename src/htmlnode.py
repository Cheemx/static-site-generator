class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        pass
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " " + " ".join([f"{key}=\"{value}\"" for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode('{self.tag}', '{self.value}', children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if not self.value and self.tag not in {'img', 'br', 'hr'}:
            raise ValueError(f"LeafNode value is missing: {self}")
        if self.tag == None:
            return self.value
        if self.tag in {'img', 'br', 'hr'}:
            return f"<{self.tag}{self.props_to_html()} />"
        html_tag = f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        return html_tag
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("tag is a required argument")
        if not self.children:
            raise ValueError("children are required argument")
        
        children_html = ""

        for child in self.children:
            children_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"   