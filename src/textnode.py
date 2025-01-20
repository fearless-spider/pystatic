from enum import Enum


class TextType(Enum):
    BOLD = "bold"


class TextNode:
    def __init__(self, text, text_type, url=None):
        super().__init__()
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
