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
    ll.insertAfter(1,2)
    ll.append(5)
    ll.insertBefore(1,7)
    assert ll.__str__() == '3->2->7->1->2->5->None'



def test_includes():
    ll = LinkedList()
    ll.insert(7)
    ll.insert(2)
    assert ll.includes(7) == True
    assert ll.includes(47) == False



def test_kthFromEnd():
    ll = LinkedList()
    ll.kthFromEnd(0) == 'k number out of the range '
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insertAfter(1,2)
    ll.append(5)
    ll.insertBefore(1,7)
    ll.insert(2)                       #'3->2->7->1->2->5->None'
    assert ll.kthFromEnd(0) == 5
    assert ll.kthFromEnd(1) == 2
    assert ll.kthFromEnd(100) == 'k number out of the range '









    

