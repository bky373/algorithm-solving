n = int(input())
for _ in range(n):
    lst = input().split()
    print(' '.join([l[::-1] for l in lst]))
