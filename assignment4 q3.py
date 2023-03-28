from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes_at_level(root, level):
    if root is None:
        return 0
    queue = deque([(root, 0)])
    count = 0
    while queue:
        node, node_level = queue.popleft()
        if node_level == level:
            count += 1
        elif node_level > level:
            break
        if node.left is not None:
            queue.append((node.left, node_level + 1))
        if node.right is not None:
            queue.append((node.right, node_level + 1))
    return count

# Example usage
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(count_nodes_at_level(root, 2)) # Output: 2

    

