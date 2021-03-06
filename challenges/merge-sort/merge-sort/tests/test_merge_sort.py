from merge_sort import __version__
from merge_sort.merge_sort import Mergesort

def test_version():
    assert __version__ == '0.1.0'



def test_sample():
    arr = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = Mergesort(arr)
    assert actual == expected


def test_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    expected = [-2,5,8,12,18,20]
    actual = Mergesort(arr)
    assert actual == expected
    

def test_few_uniques():
    arr = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = Mergesort(arr)
    assert actual == expected
    

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = Mergesort(arr)
    assert actual == expected
    
