class Ktree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None


    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def print_tree(self):
        
        
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = Ktree(1)

    laptop = Ktree(2)
    laptop.add_child(Ktree(3))
    laptop.add_child(Ktree(4))
    laptop.add_child(Ktree(5))

    cellphone = Ktree(6)
    cellphone.add_child(Ktree(7))
    cellphone.add_child(Ktree(8))
    cellphone.add_child(Ktree(9))

    tv = Ktree(10)
    tv.add_child(Ktree(11))
    tv.add_child(Ktree(12))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
    return root

    
    
def new_k_tree(arr):
    root = Ktree(arr[0].data)

    laptop = Ktree(arr[1].data)
    laptop.add_child(arr[2].data)
    laptop.add_child(Ktree(arr[3].data))
    laptop.add_child(Ktree(arr[4].data))

    cellphone = Ktree(arr[5].data)
    cellphone.add_child(arr[6].data)
    cellphone.add_child(Ktree(arr[7].data))
    cellphone.add_child(Ktree(arr[8].data))

    tv = Ktree(arr[9].data)
    tv.add_child(arr[10].data)
    tv.add_child(Ktree(arr[11].data))
    tv.add_child(Ktree(arr[12].data))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
    return root



def fizz_buzz_tree(k_tree):
    
    arr=k_tree.children
    for i in arr:
        if i.data % 3 == 0:
            i.data = 'Fizz'
        elif i.data % 5 ==0:
            i.data = 'Buzz'
        elif i.data % 3 == 0 and i.data % 5 == 0:
            i.data = 'FizzBuzz'
        else:
            i.data = 'obada'
    return new_k_tree(arr)



    

if __name__ == '__main__':
    oldtree=build_product_tree()
    fizz_buzz_tree(oldtree)

