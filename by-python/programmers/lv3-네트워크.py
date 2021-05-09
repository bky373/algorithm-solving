from collections import deque


def bfs(start, computers, tour):
    tour[start] = 1

    q = deque([start])

    while q:
        now = q.popleft()
        for i in range(len(computers[now])):
            if not tour[i] and computers[now][i] == 1:
                tour[i] = 1
                q.append(i)


def solution(n, computers):
    tour = [0] * n

    answer = 0
    for i in range(n):
        if not tour[i]:
            answer += 1
            bfs(i, computers, tour)

    return answer


res = solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
print(res)
