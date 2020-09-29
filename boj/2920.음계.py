data = list(map(int, input().split()))

output = "mixed"
for x in range(len(data)-1):
    if data[x] == data[x+1] - 1:
        output = "ascending"
    elif data[x] == data[x+1] + 1:
        output = "descending"
    else:
        output = "mixed"
        break
print(output)