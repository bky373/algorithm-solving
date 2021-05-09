import sys

n = int(input())
k = int(input())

if k >= n:
    print(0)
    sys.exit()

data = list(map(int, input().split()))
data.sort()

distances = []
for i in range(1, n):
    distances.append(data[i] - data[i - 1])
distances.sort(reverse=True)

for i in range(k - 1):
    distances[i] = 0
print(sum(distances))
