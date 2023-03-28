from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)

def has_cycle(graph):
    visited = {v: False for v in graph.vertices}
    stack = {v: False for v in graph.vertices}
    for vertex in graph.vertices:
        if not visited[vertex]:
            if dfs_traversal(graph, vertex, visited, stack):
                return True
    return False

def dfs_traversal(graph, vertex, visited, stack):
    visited[vertex] = True
    stack[vertex] = True
    for neighbour in graph.adj_list[vertex]:
        if not visited[neighbour]:
            if dfs_traversal(graph, neighbour, visited, stack):
                return True
        elif stack[neighbour]:
            return True
    stack[vertex] = False
    return False

# Example usage
if __name__ == '__main__':
    graph = Graph([0, 1, 2, 3])
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    print(has_cycle(graph)) # Output: True
