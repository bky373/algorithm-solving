n, m, v = map(int, input().split())
graph = []

for _ in range(m):
    a, b = map(int, input().split())
    graph.append((a, b))
    graph.append((b, a))

graph.sort(reverse=True)
visited = [False] * n
queue = [v]

# DFS
while queue:
    value = queue.pop()
    if not visited[value-1]:
        visited[value-1] = True
        print(value, end=' ')
        for i in range(len(graph)):
            if graph[i][0] == value:
                queue.append(graph[i][1])

print()

graph.sort()
visited = [False] * n
queue = [v]

# BFS
while queue:
    value = queue.pop(0)
    if not visited[value-1]:
        visited[value-1] = True
        print(value, end=' ')
        for i in range(len(graph)):
            if graph[i][0] == value:
                queue.append(graph[i][1])
