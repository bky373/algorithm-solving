import sys

input = sys.stdin.readline

N = int(input())
lowest = [100.000] * 7

for i in range(N):
    score = float(input().replace("\n", ""))

    lowest.sort()

    if lowest[-1] > score:
        lowest[-1] = score

lowest.sort()
for score in lowest:
    print("{:<.3f}".format(score))
