# class Node:
# 	def __init__(self,data=None,next=None):  #have two class mempers
# 		self.data = data
# 		self.next = next         

# class LinkedList:
    
	
	
# 	def __init__(self):
# 		self.head = None
    
    


# 	def insert(self,data):
# 		node = Node(data,self.head)
# 		self.head = node                          

# 	def __str__(self):
# 		if self.head is None:
			
# 			return('linked list is empty')
			
		
# 		itr = self.head
		
# 		llstr = ''
# 		while itr:
# 			llstr += str(itr.data) + '->'
# 			itr = itr.next
# 		print(llstr + f"{itr}") 
# 		return(llstr + f"{itr}") 

	
# 	def includes(self,data):
# 		if not self.head:
# 			return False

# 		else:
# 			cur =self.head
# 			while cur != None:
# 				if cur.data == data:
# 					return True

# 				else:
# 					cur = cur.next

# 			return False
    
# 	def append(self,value):

#          if self.head is None:
#             self.head = Node(value, None)
#             return

#          itr = self.head   

#          while itr.next:
#             itr = itr.next     

#          itr.next = Node(value, None)


	
# 	def insertBefore(self,value, newVal):

# 		count = self.head
# 		if count.data == value:
# 			self.insert(newVal)
		
# 		else:
# 			while count:
# 				if count.next.data==value:
# 					nextVal=count.next
# 					count.next=Node(newVal,None)
# 					count.next.next=nextVal
# 					break
# 				count=count.next

  
# 	def insertAfter(self,value, newVal):

# 		count = self.head

# 		while count:
# 			if count.data==value:
# 				nextVal=count.next
# 				count.next=Node(newVal,None)
# 				count.next.next=nextVal
# 				break
# 			count=count.next

# 	def kthFromEnd(self,k):
# 		newArr=[]
# 		itr = self.head        
# 		while itr:
# 			newArr.append(itr.data)
# 			itr = itr.next

# 		if newArr == [] or k > len(newArr):
# 			return('k number out of the range ')

# 		else:

# 		    newArr.reverse()
# 		    return(newArr[k])

	
# 	def insertValus(self,arr):

# 		for i in arr:
# 			self.append(i)

# 	def insertValusRevese(self,arr):

# 		count = len(arr)-1

# 		for i in arr:
			
# 			self.append(arr[count])
# 			count+=- 1


 

# def zipLists(arg1,arg2):
#   ll1=arg1.replace('None', '')
#   ll2=arg2.replace('None', '')

  
#   ll3=ll1.split('->')
#   ll4=ll2.split('->')

#   llall=[]

#   if len(ll3) <= len(ll4) :
# 	      for i in range(len(ll3)):
# 		      llall+=ll3[i]+ll4[i]
# 	      llall+=ll4[len(ll3):len(ll4)-1]


#    ------------------------------------------------------------ 
#   if len(ll4) < len(ll3) :
	
# 	      for i in range(len(ll4)):
# 		      llall+=ll3[i]+ll4[i]
# 	      llall+=ll3[len(ll4):len(ll3)-1]

#   return(llall)

# if __name__ == '__main__':
# 	# ll1 = LinkedList()
# 	# ll2 = LinkedList()
# 	# ll3 = LinkedList()
	

# 	# ll1.insertValus([1,2,3])
# 	# ll2.insertValus([4,5,6,8])
# 	# arg1=ll1.__str__()
# 	# arg2=ll2.__str__()

# 	# ll3.insertValus(zipLists(arg1,arg2))
# 	# arg3=ll3.__str__()

# 	ll = LinkedList()
# 	ll.insertValusRevese([1,2,3])
# 	ll.__str__()
	# ll.kthFromEnd(0)
	# ll.kthFromEnd(2)
class Node:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next


class LinkedList:
	def __init__(self):
		self.head=None
	def insertatbigining(self,data):
		node = Node(data,self.head)
		self.head = node

	def print(self):
		if self.head==None:
			print('no linked list')
		itr = self.head
		llstt = ''
		while itr:
			llstt += str(itr.data) + '->'
			itr = itr.next

		print(llstt)
	

	def insertatend(self,data):
		if self.head is None:
			self.head = Node(data,None)

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data,None)



	def inserValues(self,values):
		 self.head = None
		 for i in values:
			 self.insertatbigining(i)

	
	def length(self):
		count = 0

		itr = self.head
		while itr:
			itr=itr.next
			count+=1
			
		
		return(count)

	
	def remove(self,index):
		if index < 0 or index >= self.length():
			raise Exception('not vaild index')

		if index == 0:
			self.head = self.head.next

		count = 0

		itr= self.head
		while itr:
			if count == index -1:
				itr.next= itr.next.next
				break


			itr = itr.next
			count += 1

	def insertatindex(self,index,data):
		if index < 0 or index >= self.length():
			raise Exception('not vaild index')

		if index == 0:
			self.head = self.head.next

		count = 0

		itr= self.head
		while itr:
			if count == index -1:
				node = (data,itr.next)
				itr.next= node
				break


			itr = itr.next
			count += 1

		
	

	


		


if __name__ == '__main__':
	ll = LinkedList()
	ll.inserValues([1,2,3,4])
	ll.print()
	ll.remove(2)
	ll.print()
	





