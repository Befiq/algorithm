from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A','D'],
    'C': ['A','E'],
    'D': ['B'],
    'E': ['C']
}

graph['F'] = ['A','D']
graph['A'].append('F')
graph['D'].append('F')

def get_neighbors(graph, node):
    return graph.get(node, [])

print(get_neighbors(graph, 'A'))


def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node,end = '')
            visited.add(node)

            for neighbor in reversed(graph[node]):
                stack.append(neighbor)


def bfs(graph,start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node,end=' ')
            visited.add(node)

            for neighbor in graph[node]:
                queue.append(neighbor)

                
