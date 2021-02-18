def solve():
    for i in range(len(edges)):
        for j in range(len(edges)):
            A, B = edges[i]
            C, D = edges[j]

            if A == C or A == D or B == C or B == D:
                continue

            if matrix[B][C] != 1:
                continue

            for E in lists[D]:
                if E == A or E == B or E == C or E == D:
                    continue
                print(1)
                return
    print(0)


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = [[0] * (N) for _ in range(N)]
    lists = [[] for _ in range(N)]
    edges = []

    for _ in range(M):
        a, b = map(int, input().split())

        matrix[a][b] = 1
        matrix[b][a] = 1

        lists[a].append(b)
        lists[b].append(a)

        edges.append((a, b))
        edges.append((b, a))

    solve()
    # for m in matrix:
    #     print(m)
    # 
    # for l in lists:
    #     print(l)
    # 
    # for e in edges:
    #     print(e)
