def insertion_sort(data):
    for x in range(len(data)-1):
        for y in range(x+1, 0, -1):
            if data[y] < data[y-1]:
                data[y-1], data[y] = data[y], data[y-1]
            else:
                break
    return data

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

nums = insertion_sort(data)
print('\n'.join([str(n) for n in nums]))
