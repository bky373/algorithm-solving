def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    root1 = find(x)
    root2 = find(y)

    if root1 != root2:
        parents[root2] = root1
        numbers[root1] += numbers[root2]

tc = int(input())

for _ in range(tc):
    parents = dict()
    numbers = dict()

    f = int(input())
    
    for _ in range(f):
        x, y = input().split()
        
        if x not in parents:
            parents[x] = x
            numbers[x] = 1
        if y not in parents:
            parents[y] = y
            numbers[y] = 1

        union(x, y)

        print(numbers[find(x)])
