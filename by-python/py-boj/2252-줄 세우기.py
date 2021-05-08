"""
- 큐와 indegree의 수를 이용한 방법
- 학습 참고(1): https://m.blog.naver.com/ndb796/221236874984 (나동빈님 블로그)
"""


def topological_sort(degrees):
    q = []
    for i in range(1, n + 1):
        # 차수가 0인 노드를 큐에 삽입
        if degrees[i] == 0:
            q.append(i)

    # n개의 노드를 방문하면 정렬 완료
    for i in range(1, n + 1):
        if not q: return  # 다 방문하기 전에 큐가 비면 사이클이 발생한 것

        now = q.pop(0)
        res_line[i - 1] = now
        for new in adj[now]:
            degrees[new] -= 1  # 연결된 간선 삭제
            if degrees[new] == 0:  # 차수가 0이 되면 큐에 삽입
                q.append(new)

    print(' '.join(map(str, res_line)))


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    res_line = [0] * n

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        degrees[b] += 1

    topological_sort(degrees)



"""
- 스택과 DFS를 이용한 방법
- 학습 참고(2): https://jason9319.tistory.com/93
"""
# def dfs(x):
#     global st
#     tour[x] = 1
#
#     for new in adj[x]:
#         if tour[new]: continue
#         dfs(new)
#
#     st.append(x)
#
#
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     adj = [[] for _ in range(n + 1)]
#     tour = [0] * (n + 1)
#     st = []
#
#     for _ in range(m):
#         a, b = map(int, input().split())
#         adj[a].append(b)
#
#     for i in range(1, n + 1):
#         if not tour[i]:
#             dfs(i)
#
#     while st:
#         print(st.pop(), end=' ')
