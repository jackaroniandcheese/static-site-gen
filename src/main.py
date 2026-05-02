from textnode import TextNode, TextType
import os
import os.path as p
import shutil

def main():
    tn = TextNode("dummy text", TextType.TEXT)
    print(tn)

def copy_contents(subdirectory):
    print("Checking if subdirectory exists")
    if p.exists("../public"):
        print("Deleting public")
        shutil.rmtree("../public")


main()
