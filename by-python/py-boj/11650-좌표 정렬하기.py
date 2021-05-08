
n = int(input())
positions = []
for _ in range(n):
    data = input().split()
    positions.append((int(data[0]), int(data[1])))

positions_sorted = sorted(positions)

for p in positions_sorted:
    print(p[0], p[1])
