class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p :
            level = 1
            p = p.parent

        return level

    def print_tree(self):
        print(self.data)
        if len(self.children):
            for child in self.children:
                child.print_tree()

    

def build_product_tree():
    root = TreeNode('Electrinics')

    laptop = TreeNode('laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellPhone = TreeNode('cellPhone')
    cellPhone.add_child(TreeNode('iphone'))
    cellPhone.add_child(TreeNode('Google Pixel'))
    cellPhone.add_child(TreeNode('Vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('samsung'))
    tv.add_child(TreeNode('lg'))

    root.add_child(laptop)
    root.add_child(cellPhone)
    root.add_child(tv)

            

    return root





if __name__ == '__main__':
   root =  build_product_tree()
   print(root.get_level())
#    root.print_tree()

   pass