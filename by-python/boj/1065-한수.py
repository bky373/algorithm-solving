n = int(input())

cnt = 0
for i in range(1, n + 1):
    a = i // 1000
    b = i // 100 - (i // 1000) * 10
    c = i // 10 - (i // 100) * 10
    d = i % 10

    if 1 <= i <= 99:
        cnt += 1

    elif 100 <= i <= 999:
        if (b - c) == (c - d):
            cnt += 1
    else:
        if ((a - b) == (b - c)) and ((b - c) == (c - d)):
            print(3)
            cnt += 1

print(cnt)
