V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
parent = list(range(V + 1))
rank = [1 for _ in range(V + 1)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

mst = []

for edge in edges:
    A, B, weight = edge
    if find(A) != find(B):
        union(A, B)
        mst.append(weight)

print(sum(mst))
