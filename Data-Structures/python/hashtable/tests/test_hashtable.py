from hashtable import __version__
from hashtable.hashtable import HashTable


def test_version():
    assert __version__ == '0.1.0'

def test_hash():
    t= HashTable()
    actual = t.hash('march 6')
    expected = 9
    assert actual == expected

def test_add():
    t= HashTable()
    actual = t.add('march 6',130)
    expected = [('march 6', 130)]
    assert actual == expected

def test_get():
    t= HashTable()
    t.add('march 6',130)
    actual = t.get('march 6')
    expected = 130
    assert actual == expected

def test_contains():
    t= HashTable()
    t.add('march 6',130)
    actual = t.contains('march 6')
    expected = True
    assert actual == expected




