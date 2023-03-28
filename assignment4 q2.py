from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)

def dfs_traversal(graph):
    visited = {v: False for v in graph.vertices}
    for vertex in graph.vertices:
        if not visited[vertex]:
            dfs_helper(graph, vertex, visited)

def dfs_helper(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=' ')
    for neighbour in graph.adj_list[vertex]:
        if not visited[neighbour]:
            dfs_helper(graph, neighbour, visited)

# Example usage
if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3, 4])
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    dfs_traversal(graph) # Output: 0 1 2 3 4
