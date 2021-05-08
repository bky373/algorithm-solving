X = int(input())

sticks = [64, 32, 16, 8, 4, 2, 1]
cnt, total = 0, 0
i = 0
while True:
    if X == total:
        print(cnt)
        break
    if X >= total + sticks[i] :
        total += sticks[i]
        cnt += 1
    i += 1
    