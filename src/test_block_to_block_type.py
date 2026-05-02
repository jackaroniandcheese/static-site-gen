import unittest
from block_markdown import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):

    def test_h1(self):
        h1 = "# This is h1"
        self.assertEqual(
            block_to_block_type(h1),
            BlockType.HEADING,
        )

    def test_h6(self):
        h6 = "###### This is h6"
        self.assertEqual(
            block_to_block_type(h6),
            BlockType.HEADING,
        )

    def test_h7(self):
        h7 = "####### This is h7"
        self.assertEqual(
            block_to_block_type(h7),
            BlockType.PARAGRAPH,
        )

    def test_code(self):
        code = """```
print("Hello World!")
```"""
        self.assertEqual(
            block_to_block_type(code),
            BlockType.CODE,
        )

    def test_quote_no_space(self):
        quote = """>
>Live laugh love
>Love laugh live"""
        self.assertEqual(
            block_to_block_type(quote),
            BlockType.QUOTE,
        )

    def test_quote_space(self):
        quote = """> 
> Live laugh love
> Love laugh live"""
        self.assertEqual(
            block_to_block_type(quote),
            BlockType.QUOTE,
        )

    def test_quote_mixed_space(self):
        quote = """>
> Live laugh
>Love"""
        self.assertEqual(
            block_to_block_type(quote),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        ul = """- Groceries
- Dishes
- Make Bed"""
        self.assertEqual(
            block_to_block_type(ul),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        ol = """1. Groceries
2. Dishes
3. Make Bed"""
        self.assertEqual(
            block_to_block_type(ol),
            BlockType.ORDERED_LIST,
        )
