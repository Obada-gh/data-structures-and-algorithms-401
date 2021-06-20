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


    def peek(self):
        if self.top is None:
            raise Exception('empty stack')
        tempNode = self.top
        
        return tempNode.value

    
    def isEmpty(self):
        if self.top is None:
            return True

    
class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()
        

    def enqueue(self,value=None):
        if value == None:
            return 'value is None'
        self.front.push(value)


    def dequeue(self):
        if self.front.top == None:
            raise Exception('empty queue')
        while self.front.top:
            self.rear.push(self.front.pop())
        dequeueVal= self.rear.pop()

        while self.rear.top:
            print(self.rear.top.value)
            self.front.push(self.rear.pop())
        return dequeueVal

    
    def __str__(self):
        cur = self.front.top
        llstr=''
        while cur:
            if not cur.next:
                llstr=llstr+f'{cur.value}'
                cur = cur.next
            else:
                llstr=llstr+f'{cur.value}->'
                cur = cur.next
            
        print(llstr)

        return llstr

    

        
  


    def peek(self):
        if self.front is None:
            raise Exception('empty queue')
        node = self.front
        print (node.value)
        return node.value

    
    def isEmpty(self):
        return self.front == None








if __name__ == '__main__':
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.__str__()









        