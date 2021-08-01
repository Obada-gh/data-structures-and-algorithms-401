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
    def add_edge(self,ver1,ver2,w):
        # check if both in graph
        edge = Edge(ver2,w)
        self.adjacencyList[ver1].append(edge)

        
    def get_nodes(self):
        pass
    def get_neighbors(self):
        pass    
    def size(self):
        pass



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


 



