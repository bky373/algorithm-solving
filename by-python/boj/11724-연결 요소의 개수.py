import sys
sys.setrecursionlimit(10000000)

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def dfs(v):
    if visited[v]:
        return 0

    visited[v] = True
    for k in adj[v]:
        if not visited[k]:
            dfs(k)
    return 1


result = 0
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
    adj[y].append(x)

for i in range(1, n + 1):
    result += dfs(i)

print(result)
