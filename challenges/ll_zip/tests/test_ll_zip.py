from ll_zip import __version__


def test_version():
    assert __version__ == '0.1.0'



from ll_zip.ll_zip import LinkedList ,zipLists






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


def test_mergedLinkedLists():

    ll1 = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList()
	

    ll1.insertValus([1,2,3])
    ll2.insertValus([4,5,6,8])
    arg1=ll1.__str__()
    arg2=ll2.__str__()

    ll3.insertValus(zipLists(arg1,arg2))
    arg3=ll3.__str__()

    assert arg3 == '1->4->2->5->3->6->8->None'

