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
			
			return('linked list is empty')
			
		
		itr = self.head
		
		llstr = ''
		while itr:
			llstr += str(itr.data) + '->'
			itr = itr.next
		print(llstr + f"{itr}") 
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

	def kthFromEnd(self,k):
		newArr=[]
		itr = self.head        
		while itr:
			newArr.append(itr.data)
			itr = itr.next

		if newArr == [] or k > len(newArr):
			return('k number out of the range ')

		else:

		    newArr.reverse()
		    return(newArr[k])

	
	def insertValus(self,arr):

		for i in arr:
			self.append(i)


# def zipLists(ll1, ll2):
def zipLists(ll1,ll2):
    cur1 = ll1.head
    cur2 = ll2.head

    if cur1 == None or cur2 == None:
        if cur1:
            return ll1.__str__()
        elif cur2:
            return ll2.__str__()
        else:
         return 'two linked list are empty'

    newArr = []
    while cur1 or cur2:
        if cur1 :
            newArr+=[cur1.data]
            cur1 = cur1.next
        if cur2 :
            newArr+=[cur2.data]
            cur2 = cur2.next
    mergedLinkedlist=''
    for i in newArr:
      mergedLinkedlist+=f'{i}->'
    mergedLinkedlist+="None"
    return mergedLinkedlist




    
    
if __name__ == '__main__':
	ll1 = LinkedList()
	ll2 = LinkedList()

	ll1.append(1)
	ll1.append(2)
	ll1.append(3)
	ll1.append(4)


	ll2.append(1)
	ll2.append(2)
	ll2.append(3)
	ll2.append(4)

	print(zipLists(ll1, ll2))


	



	
	
	    
		


	
	
