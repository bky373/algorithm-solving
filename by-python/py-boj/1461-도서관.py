import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
positive = []
negative = []

longest = max(max(arr), -min(arr))

for i in arr:
    if i > 0:
        heapq.heappush(positive, -i)
    else:
        heapq.heappush(negative, i)

result = 0
while positive:
    result += heapq.heappop(positive)
    for _ in range(m - 1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)

print(-result * 2 - longest)
