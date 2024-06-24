class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            raise Exception("Props is empty")
        listP = []
        for key, value in self.props.items():
            listP.append(f'{key}="{value}"')
        return " ".join(listP)
    
    def __repr__(self):
        return f"Tag= {self.tag} Value= {self.value} Children= {self.children} Props= {self.props}"
    