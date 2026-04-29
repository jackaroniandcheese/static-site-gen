import unittest
from inline_markdown import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
                "This is text with a [url](boot.dev) and a [link to youtube](youtube.com)"
                )
        self.assertListEqual([("url", "boot.dev"), ("link to youtube", "youtube.com")], matches)

    def test_link_red_herring(self):
        matches = extract_markdown_links(
                "This is [a red herring because no link follows]. This is now [real alt text](withareallink.com)"
                )
        self.assertListEqual([("real alt text", "withareallink.com")], matches)

    #Courtesy of Boots:
    def test_links_ignore_images(self):
        matches = extract_markdown_links("![image](img.png)")
        self.assertListEqual([], matches)

    def test_empty_link_text(self):
        matches = extract_markdown_links("[](boot.dev)")
        self.assertListEqual([("", "boot.dev")], matches)
