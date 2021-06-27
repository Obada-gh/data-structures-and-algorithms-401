# # in order traversal : your root in the middle you visit the left tree then right tree
# [7,12,14,15,20,23,27,88]
# # pre order traversal: your root first then left tree then right tree
# [15,12,7,14,27,20,23,88]
# # post order traversal: your root at the end then left tree then right tree 
# [7,14,12,23,20,88,27,15]
# # remember the child is root for the element below.

class Binary_Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self,value):
        if value == self.value:
            return
        if value < self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = Binary_Tree(value)
        
        if value > self.value:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = Binary_Tree(value)
    
    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        elements.append(self.value)

        if self.right:
            elements += self.right.in_order()
        
        return elements

    def pre_order(self):
        elements = []
        if self.left:
            elements += self.left.pre_order()
        elements.append(self.value)

        if self.right:
            elements += self.right.pre_order()
        
        return elements

    def post_order(self):
        elements = []
        if self.left:
            elements += self.left.post_order()
        elements.append(self.value)

        if self.right:
            elements += self.right.post_order()
        
        return elements

    def contains(self,value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        if value > self.value:
            if self.right:
                return self.right.contains(value)
            else:
                return False
        

def build_tree(elements):
    root = Binary_Tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    nums = [17,4,1,20,9,23,18,34,18,4]
    nums_tree = build_tree(nums)
    print(nums_tree.in_order())
    print(nums_tree.contains(5))
            





# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)
    
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p :
#             level = 1
#             p = p.parent

#         return level

#     def print_tree(self):
#         print(self.data)
#         if len(self.children):
#             for child in self.children:
#                 child.print_tree()

    

# def build_product_tree():
#     root = TreeNode('Electrinics')

#     laptop = TreeNode('laptop')
#     laptop.add_child(TreeNode('Mac'))
#     laptop.add_child(TreeNode('Surface'))
#     laptop.add_child(TreeNode('Thinkpad'))

#     cellPhone = TreeNode('cellPhone')
#     cellPhone.add_child(TreeNode('iphone'))
#     cellPhone.add_child(TreeNode('Google Pixel'))
#     cellPhone.add_child(TreeNode('Vivo'))

#     tv = TreeNode('TV')
#     tv.add_child(TreeNode('samsung'))
#     tv.add_child(TreeNode('lg'))

#     root.add_child(laptop)
#     root.add_child(cellPhone)
#     root.add_child(tv)

            

#     return root





# if __name__ == '__main__':
#    root =  build_product_tree()
#    print(root.get_level())
# #    root.print_tree()

#    pass

        

