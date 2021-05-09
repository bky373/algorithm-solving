tc = int(input())


def dfs(num):
    if adj[num] == num:
        visited[num] = True
        return 1

    if visited[num]:
        return 0

    visited[num] = True
    if not visited[adj[num]]:
        dfs(adj[num])

    return 1


for _ in range(tc):
    n = int(input())
    input_array = list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        adj[i] = input_array[i - 1]

    result = 0
    for i in range(1, n + 1):
        result += dfs(i)

    print(result)
