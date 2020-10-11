import sys

n = int(sys.stdin.readline())
MAX = 1_000_000
negatives = [0 for _ in range(MAX + 1)]
positives = [0 for _ in range(MAX + 1)]

for _ in range(n):
    number = int(sys.stdin.readline())
    if number >= 0:
        positives[number] += 1
    else:
        negatives[-number] += 1

for x in range(MAX, -1, -1):
    if negatives[x] >= 1:
        print(-x)
for x in range(MAX + 1):
    if positives[x] >= 1:
        print(x)
