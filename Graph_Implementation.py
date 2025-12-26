# Implementation of graph 

graph = {
    1 : [2],
    2 : [3,4],
    3 : [7,4],
    4 : [5],
    5 : [],
    6 : [5],
    7 : [6]
}



#Breadth First Search
visited_bfs = []
queue = []
def BFS(visited, graph, node):

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    
    return visited

#Depth First Search
visited_dfs = []
stack = []
def DFS(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            DFS(visited, graph, n)
    return visited


print('BFS of the given graph:')
print(BFS(visited_bfs, graph, 1))
print("\nDFS of the given graph:")
print(DFS(visited_dfs, graph, 1))