#------------------------queue for breadthFirst method

from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


#___________________________________________________________




class Node:
    def __init__(self,val):
        self.val=val
    
class Edge:
    def __init__(self, node, w):
        self.node = node
        self.w = w


class Graph:
    def __init__(self):
        self.adjacencyList = {}
    def add_node(self,val):
        v = Node(val)
        self.adjacencyList[v] = []
        return v
    def add_edge(self,start,end,w=0):
        # check if both in graph
        edge = Edge(end,w)
        self.adjacencyList[start].append(edge)

        
    def get_nodes(self):
        allNodes = []

        for node in self.adjacencyList.keys():
            allNodes.append(node)

        return allNodes


    def get_neighbors(self,node):
        neighbors = []
        if node in self.adjacencyList:
        
            for neighbor in self.adjacencyList[node]:
                neighbors.append((neighbor.node,neighbor.w))  
        
        return neighbors
    def size(self):

        return len(self.adjacencyList.keys())

    def __str__(self):
        output = ''
        for node in self.adjacencyList.keys():
            # Concatenate the value of node
            output += node.val
            # Iterate over all edges of this node
            for edge in self.adjacencyList[node]:
                output += ' -> ' + edge.node.val 
            # Add a new line
            output += '\n'
        return output
    
    def breadthFirst(self,node):
        nodes = []
        breadth= Queue()
        visited = set()

        breadth.enqueue(node)
        visited.add(node)

        while breadth:
            front = breadth.dequeue()
            nodes.append(front)

            for child in self.adjacencyList[front]:
                if child.node not in visited:
                    child = child.node
                    visited.add(child)
                    breadth.enqueue(child)
        
        return nodes
    

def business_trip(graph,arr):
    exist = True
    cost = 0
    for i in range(len(arr)-1):
        for j in graph.get_neighbors(arr[i]):
            if arr[i+1] == j[0]:
                cost+=j[1]
                exist=True
                break
            else:
                exist = False
    
    if cost == 0 :
        exist = False

    return f'{exist} {cost} $'                











if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, b,150)
    graph.add_edge(b, a,150)
    graph.add_edge(a, c,82)
    graph.add_edge(c, a,82)
    graph.add_edge(b, d,99)
    graph.add_edge(d, b,99)
    graph.add_edge(c, d,42)
    graph.add_edge(d, c,42)
    graph.add_edge(c, e,105)
    graph.add_edge(e, c,105)
    graph.add_edge(d, f,26)
    graph.add_edge(f, d,26)
    

    print(graph.breadthFirst(a))
    print(business_trip(graph,[a,b,d]))










   



 



