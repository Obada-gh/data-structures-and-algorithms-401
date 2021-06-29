class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 


class Binary_tree:
    def __init__(self):
        self.root = None
        self.tree = []


def breadth_first(tree):
    arr = [tree.root]
    arr2 = []
    if tree.root==None:
        return 'empty tree'
    
    while arr:
        
        node=arr[0]
        if node.left:
            arr+=[node.left]

        if node.right:
            arr+=[node.right]

        arr2+=[arr[0].value]
        arr=arr[1:]
        
    return arr2

if __name__ == '__main__':
    tree = Binary_tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(breadth_first(tree))
    


        

    

        