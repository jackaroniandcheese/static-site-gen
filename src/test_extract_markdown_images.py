import unittest
from inline_markdown import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/justkidding)"
                )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://i.imgur.com/justkidding")], matches)

    def test_image_red_herring(self):
        matches = extract_markdown_images(
                "This is ![a red herring because no link follows]. This is now ![real alt text](withareallink.com)"
                )
        self.assertListEqual([("real alt text", "withareallink.com")], matches)

    # Courtesy of Boots:
    def test_no_images(self):
        matches = extract_markdown_images("just plain text")
        self.assertListEqual([], matches)

    def test_empty_image_alt(self):
        matches = extract_markdown_images("![](img.png)")
        self.assertListEqual([("", "img.png")], matches)
