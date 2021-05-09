import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
graph_return = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph_return[e].append((s, w))


def dijkstra(start):
    # X 마을에서 돌아오는 경로
    distances = [INF] * (N + 1)
    distances[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist_to_now, now = heapq.heappop(heap)

        if distances[now] < dist_to_now:
            continue

        for adj, dist_now_to_adj in graph[now]:
            dist_to_adj = dist_to_now + dist_now_to_adj

            if dist_to_adj < distances[adj]:
                distances[adj] = dist_to_adj
                heapq.heappush(heap, (dist_to_adj, adj))

    # X 마을로 가는 경로
    distances_reverse = [INF] * (N + 1)
    distances_reverse[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist_to_now, now = heapq.heappop(heap)

        if distances_reverse[now] < dist_to_now:
            continue

        for adj, dist_now_to_adj in graph_return[now]:
            dist_to_adj = dist_to_now + dist_now_to_adj

            if dist_to_adj < distances_reverse[adj]:
                distances_reverse[adj] = dist_to_adj
                heapq.heappush(heap, (dist_to_adj, adj))

    return list(map(sum, zip(distances[1:], distances_reverse[1:])))


result = dijkstra(X)
print(max(result))
