n = int(input())

names = [ input() for _ in range(n)]
names_len = len(names[0])
result = ''

for i in range(names_len):
    ck = False
    for j in range(1, n):
        if names[0][i] != names[j][i]:
            ck = True
            result += '?'
            break
    if not ck:
        result += names[0][i]
print(result)
