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

	def __str__(self):
		if self.head is None:
			print('linked list is empty')
			return
		
		itr = self.head
		
		llstr = ''
		while itr:
			llstr += str(itr.data) + '->'
			itr = itr.next
		print(llstr + f"{itr}") 

	
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
	ll.append(5)
	ll.append(6)
	ll.append(6)
	ll.insertBefore(1,7)
	ll.insertAfter(1,8)
	ll.__str__()
	
    



# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")

#         if index==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count+=1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)


# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.insert_at(1,"blueberry")
#     ll.remove_at(2)
#     ll.print()

#     ll.insert_values([45,7,12,567,99])
#     ll.insert_at_end(67)
#     ll.print()



		

		



	
		






		









	

