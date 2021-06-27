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


def test_pre_order():
    nums = [17,4,1,20,9,23,18,34,18,4]
    nums_tree = build_tree(nums)
    actual = nums_tree.pre_order() 
    expected = [17, 4, 1, 9, 20, 18, 23, 34]
    assert actual == expected 


def test_post_order():
    nums = [17,4,1,20,9,23,18,34,18,4]
    nums_tree = build_tree(nums)
    actual = nums_tree.post_order() 
    expected = [1, 9, 4, 18, 34, 23, 20, 17]
    assert actual == expected 
