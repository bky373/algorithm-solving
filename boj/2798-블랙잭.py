N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' ')))
totals = []

for x in range(N-1):
    for y in range(x+1, N-1):
        for z in range(y+1, N):
            total = cards[x] + cards[y] + cards[z]
            if total <= M:
                totals.append(total)

print(max(totals))
