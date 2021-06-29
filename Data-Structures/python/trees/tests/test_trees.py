from trees import __version__
from trees.trees import *


def test_version():
    assert __version__ == '0.1.0'

def test_breadth_first():
    tree = Binary_tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    assert breadth_first(tree) == [1,2,3,4,5]
