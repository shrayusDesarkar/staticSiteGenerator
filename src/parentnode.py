from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if children is None:
            raise ValueError("Children requires a value")
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag requires a value")
        if self.children is None:
            raise ValueError("Children requires a value")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        html = f"<{self.tag}>{children_html}</{self.tag}>"
        return html
