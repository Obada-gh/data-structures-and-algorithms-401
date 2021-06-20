from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PseudoQueue,Stack,Node


def test_version():
    assert __version__ == '0.1.0'


def test_insertValues():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    actual = queue.__str__()
    expected = '4->3->2'
    assert actual == expected


#how to test the raise Exception('empty queue')

def test_NoneValue():
    expected = 'value is None'
    queue = PseudoQueue()
    actual=queue.enqueue()
    assert actual == expected


    



