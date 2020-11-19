t = int(input())

for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    d = [0] * n
    circuit_count = 0
    while True:
        for x in range(n):
            if c[x] % 2:
                c[x] = c[x] + 1
            d[x] = c[x] // 2

        if len(set(c)) == 1:
            print(circuit_count)
            break

        for x in range(1, n):
            c[x] = c[x] // 2 + d[x-1]
        c[0] = c[0] // 2 + d[-1]
        circuit_count += 1
