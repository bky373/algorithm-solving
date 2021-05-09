k = 1
result = 0

n = int(input())
while n > 0:
    if n - k >= 0:
        n = n - k
        k += 1
        result += 1
    else:
        k = 1
print(result)
