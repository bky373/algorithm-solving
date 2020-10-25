import heapq

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    tmp = heapq.heappop(heap) + heapq.heappop(heap)
    result += tmp
    heapq.heappush(heap, tmp)

print(result)
