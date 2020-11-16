n = int(input())
w = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(w):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [False] * (n+1)
def dfs(n):
    visited[n] = True
    for a in adj[n]:
        if not visited[a]:
            dfs(a)

dfs(1)
print(visited.count(True)-1)
