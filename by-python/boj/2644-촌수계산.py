from collections import deque


def bfs(start):
    q = deque([start])
    tour[start] = 1

    while q:
        now = q.popleft()
        if now == target_y:
            return steps[now]

        for adj in relationships[now]:
            steps[adj] = steps[now] + 1
            if not tour[adj]:
                q.append(adj)
                tour[adj] = 1
    return -1


if __name__ == '__main__':
    n = int(input())
    target_x, target_y = map(int, input().split())
    m = int(input())
    relationships = [[] for _ in range(n + 1)]
    steps = [0] * (n + 1)
    tour = [0] * (n + 1)
    
    for _ in range(m):
        parent, child = map(int, input().split())
        relationships[parent].append(child)
        relationships[child].append(parent)

    print(bfs(target_x))
