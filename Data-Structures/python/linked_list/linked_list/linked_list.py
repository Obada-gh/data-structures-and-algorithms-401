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
		return(llstr) 

	
	def include(self,data):
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
		 	





if __name__ == '__main__':
	ll = LinkedList()
	ll.insert(1)
	ll.insert(2)
	ll.insert(3)
	ll.toString()






	

