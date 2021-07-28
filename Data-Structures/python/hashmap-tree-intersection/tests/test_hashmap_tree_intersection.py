from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.treeHash import tree_intersection,build_tree


def test_version():
    assert __version__ == '0.1.0'


def test_matchArr():
    nums1 = [17,4,1,20,9,23,18,34,18,4]
    nums2 = [88,8,77,44,9,55,18,99,18,4]
    nums_tree1 = build_tree(nums1)
    nums_tree2 = build_tree(nums2)
    expected=[4, 9, 18]
    actual=tree_intersection(nums_tree1,nums_tree2)
    assert actual == expected


