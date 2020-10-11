import sys

n = int(input())
nums = [0] * 10001
for _ in range(n):
    x = int(sys.stdin.readline())
    nums[x] += 1

for x in range(1, 10001):
    if nums[x] != 0:
        for c in range(nums[x]):
            print(x)
