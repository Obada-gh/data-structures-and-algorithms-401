from trees import __version__
from trees.trees import Binary_Tree,build_tree


def test_version():
    assert __version__ == '0.1.0'

def test_in_order():
    nums = [17,4,1,20,9,23,18,34,18,4]
    nums_tree = build_tree(nums)
    actual = nums_tree.in_order() 
    expected = [1, 4, 9, 17, 18, 20, 23, 34]
    assert actual == expected 

def test_contains():
    nums = [17,4,1,20,9,23,18,34,18,4]
    nums_tree = build_tree(nums)
    actual = nums_tree.contains(4)
    expected = True
    assert actual == expected
    assert nums_tree.contains(5) == False
