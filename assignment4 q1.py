from collections import deque

# Define a graph class with adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in vertices}

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

# Function to perform breadth first traversal
def bfs_traversal(graph, start):
    visited = {v: False for v in graph.vertices}
    queue = deque([start])
    visited[start] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbour in graph.adj_list[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

# Example usage
if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    graph = Graph(vertices)
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')
    bfs_traversal(graph, 'A')
