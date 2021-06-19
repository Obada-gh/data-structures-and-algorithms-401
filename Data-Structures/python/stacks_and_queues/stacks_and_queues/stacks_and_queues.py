class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next


class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        node=  Node(value,self.top)
        self.top = node

    def pop(self):
        if self.top is None:
            raise Exception('empty stack')
        tempNode = self.top
        self.top = self.top.next
        tempNode.next = None
        return tempNode.value


        
    
    def __str__(self):
        if self.top is None:
            return('empty stack')
        llstr= ''
        itr=self.top
        while itr:
            llstr+=str(itr.value)
            itr = itr.next
        print(llstr + f"{itr}")
        return(llstr + f"{itr}")

    def peek(self):
        if self.top is None:
            raise Exception('empty stack')
        tempNode = self.top
        print (tempNode.value)
        return tempNode.value

    
    def isEmpty(self):
        if self.top is None:
            return True

    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node=  Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


    def dequeue(self):
        if self.front is None:
            raise Exception('empty queue')
        tempNode = self.front
        self.front = self.front.next
        tempNode.next = None
        return tempNode.value


        
    
    def __str__(self):
        if self.front is None:
            return('empty queue')
        llstr= ''
        itr=self.front
        while itr:
            llstr+=str(itr.value)
            itr = itr.next
        print(llstr + f"{itr}")
        return(llstr + f"{itr}")

    def peek(self):
        if self.front is None:
            raise Exception('empty queue')
        node = self.front
        print (node.value)
        return node.value

    
    def isEmpty(self):
        return self.front == None








if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.__str__()
    stack.pop()
    stack.__str__()
    stack.peek()

    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.__str__()
    queue.peek()
    queue.dequeue()
    queue.__str__()
    queue.isEmpty()








        