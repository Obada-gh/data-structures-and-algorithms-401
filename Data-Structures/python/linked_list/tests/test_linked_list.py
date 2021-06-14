from linked_list import __version__
from linked_list.linked_list import LinkedList , Node


def test_version():
    assert __version__ == '0.1.0'



def test_instantiate():                        
    ll = LinkedList()
    assert isinstance(ll,LinkedList)


def test_toString():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)

    assert ll.toString() == '3->2->1->'



def test_includes():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(2)
    assert ll.includes(7) == True
    assert ll.includes(47) == False









    

