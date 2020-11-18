import heapq

tc = int(input())

def dijkstra(adj, start):
    times = [ float('inf') for _ in range(n+1) ]
    times[start] = 0
    q = []
    heapq.heappush(q, [times[start], start])

    while q:
        cur_route_time, cur_com = heapq.heappop(q)

        if times[cur_com] < cur_route_time:
            continue

        for time, adjacent in adj[cur_com]:
            new_time = cur_route_time + time

            if new_time < times[adjacent]:
                times[adjacent] = new_time
                heapq.heappush(q, [new_time, adjacent])
    return times

def last_seconds(arr):
    tmp = []
    for a in arr:
        if a == float('inf'):
            continue
        tmp.append(a)
    return max(tmp)

for _ in range(tc):
    n, d, c = map(int, input().split())
    adj = [ [] for _ in range(n+1) ]

    for _ in range(d):
        a, b, s = map(int, input().split())
        adj[b].append((s, a))

    result = dijkstra(adj, c)
    print(len(result) - result.count(float('inf')), last_seconds(result))