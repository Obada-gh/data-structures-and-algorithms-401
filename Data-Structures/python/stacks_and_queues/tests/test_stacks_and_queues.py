from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Queue,Node,Stack



def test_version():
    assert __version__ == '0.1.0'


def test_Stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.__str__() == '4321None'



def test_Stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.peek()
    assert stack.peek() == 4


def test_Stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    assert stack.pop() == 3

def test_Stack_isEmpty():
    stack = Stack()
    stack.isEmpty()
    assert stack.isEmpty() == True



#Queue------------------------------------------------------------------


def test_Queue_push():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.__str__() == '1234None'



def test_Queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.peek()
    assert queue.peek() == 1


def test_Queue_pop():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    assert queue.dequeue() == 2

def test_Queue_isEmpty():
    queue= Queue()
    queue.isEmpty()
    assert queue.isEmpty() == True

