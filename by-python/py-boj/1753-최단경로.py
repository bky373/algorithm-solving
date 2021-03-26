import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]


def dijkstra(graph, start):
    distances = [INF] * (V + 1)
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist_start_to_now, now = heapq.heappop(heap)

        if distances[now] < dist_start_to_now:
            continue

        for adj, dist_now_to_adj in graph[now]:
            dist_start_to_adj = dist_start_to_now + dist_now_to_adj

            if dist_start_to_adj < distances[adj]:
                distances[adj] = dist_start_to_adj
                heapq.heappush(heap, (dist_start_to_adj, adj))
    return distances


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

result = dijkstra(graph, start)

for dist in result[1:]:
    print(dist if dist != INF else 'INF')
