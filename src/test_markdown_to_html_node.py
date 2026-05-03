import unittest

from block_markdown import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
> This is my first quote with a space after the **arrow** that won't appear because of `.strip()`
>This is my second quote with no space after the arrow that will have a space because of `.join()`
"""
    
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is my first quote with a space after the <b>arrow</b> that won't appear because of <code>.strip()</code> This is my second quote with no space after the arrow that will have a space because of <code>.join()</code></blockquote></div>"
        )

    def test_ul(self):
        md = """
- This is a list item with **bold**
- This is a list item with _italic_
"""
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list item with <b>bold</b></li><li>This is a list item with <i>italic</i></li></ul></div>",
        )

    def test_ol(self):
        md = """
1. This is list one
2. This is list two with `code`
"""
        
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is list one</li><li>This is list two with <code>code</code></li></ol></div>",
        )

    def test_heading(self):
        md = """
# heading 1

### heading 3

###### heading 6
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>heading 1</h1><h3>heading 3</h3><h6>heading 6</h6></div>",
        )
