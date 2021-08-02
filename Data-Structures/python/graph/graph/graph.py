
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
                if child[0] not in visited:
                    child = child[0]
                    visited.add(child)
                    breadth.enqueue(child)
        
        return nodes

#------------------------queue for breadthFirst method

from collections import deque

class Queue():
    def __init__(self):
        self.deque = deque()

    def enqueue(self, val):
        self.deque.appendleft(val)
    
    def dequeue(self):
        return self.deque.pop()



if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, b)
    graph.add_edge(a, c)
    graph.add_edge(b, d)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(d, f)

    print(graph.breadthFirst(a))




# if __name__ == '__main__':
#     graph = Graph()
#     a=graph.add_node('a')
#     b=graph.add_node('a')
#     a=graph.add_node('a')
#     a=graph.add_node('a')
#     a=graph.add_node('a')
#     a=graph.add_node('a')
#     a=graph.add_node('a')
# #---------------------------------------------------------------------
#   # routes = [
#     #     ("Mumbai","Pune"),
#     #     ("Mumbai", "Surat"),
#     #     ("Surat", "Bangaluru"),
#     #     ("Pune","Hyderabad"),
#     #     ("Pune","Mysuru"),
#     #     ("Hyderabad","Bangaluru"),
#     #     ("Hyderabad", "Chennai"),
#     #     ("Mysuru", "Bangaluru"),
#     #     ("Chennai", "Bangaluru")
#     # ]

# class Graph:
#     def __init__(self, edges):
#         self.edges = edges
#         self.graph_dict = {}
#         for start, end in edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end]
#         print("Graph Dict:", self.graph_dict)

#     def get_paths(self, start, end, path=[]):
#         path = path + [start]

#         if start == end:
#             return [path]

#         if start not in self.graph_dict:
#             return []

#         paths = []
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_paths = self.get_paths(node, end, path)
#                 for p in new_paths:
#                     paths.append(p)

#         return paths

#     def get_shortest_path(self, start, end, path=[]):
#         path = path + [start]

#         if start == end:
#             return path

#         if start not in self.graph_dict:
#             return None

#         shortest_path = None
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 sp = self.get_shortest_path(node, end, path)
#                 if sp:
#                     if shortest_path is None or len(sp) < len(shortest_path):
#                         shortest_path = sp

#         return shortest_path

        

        




# if __name__ == '__main__':
    
#     routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris", "Dubai"),
#         ("Paris", "New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto"),
#     ]

#     route_graph = Graph(routes)

#     start = 'Paris'
#     end = 'New York'

#     print(f'shortest paths between {start} and {end}: ',route_graph.get_shortest_path(start,end))


 



