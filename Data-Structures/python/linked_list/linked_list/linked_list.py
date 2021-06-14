class Node:
	def __init__(self,data=None,next=None):  #have two class mempers
		self.data = data
		self.next = next

class LinkedList:
	
	
	def __init__(self):
		self.head = None

	def insert(self,data):
		node = Node(data,self.head)
		self.head = node

	def toString(self):
		if self.head is None:
			print('linked list is empty')
			return
		
		itr = self.head
		
		llstr = ''
		while itr:
			llstr += str(itr.data) + '->'
			itr = itr.next
		return(llstr + f"{itr}") 

	
	def includes(self,data):
		if not self.head:
			return False

		else:
			cur =self.head
			while cur != None:
				if cur.data == data:
					return True

				else:
					cur = cur.next

			return False
    
	def append(self,value):

         if self.head is None:
            self.head = Node(value, None)
            return

         itr = self.head

         while itr.next:
            itr = itr.next

         itr.next = Node(value, None)


	
	def insertBefore(self,value, newVal):

		count = self.head
		if count.data == value:
			self.insert(newVal)
		
		else:
			while count:
				if count.next.data==value:
					nextVal=count.next
					count.next=Node(newVal,None)
					count.next.next=nextVal
					break
				count=count.next

  
	def insertAfter(self,value, newVal):

		count = self.head

		while count:
			if count.data==value:
				nextVal=count.next
				count.next=Node(newVal,None)
				count.next.next=nextVal
				break
			count=count.next


        


    
    
if __name__ == '__main__':
	ll = LinkedList()
	ll.insert(1)
	ll.insert(2)
	ll.insert(3)
	ll.insertAfter(1,2)
	ll.append(5)
	ll.insertBefore(1,7)
	
	ll.toString()
	
    




		

		



	
		






		









	

