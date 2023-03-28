def count_trees(adj_list):
    visited = {v: False for v in adj_list.keys()}
    count = 0
    for node in adj_list.keys():
        if not visited[node]:
            count += 1
            dfs(adj_list, node, visited)
    return count

def dfs(adj_list, node, visited):
    visited[node] = True
    for neighbour in adj_list[node]:
        if not visited[neighbour]:
            dfs(adj_list, neighbour, visited)

# Example usage
if __name__ == '__main__':
    adj_list = {0: [1, 2], 1: [0], 2: [0], 3: [4], 4: [3], 5: []}
    print(count_trees(adj_list)) # Output: 3
