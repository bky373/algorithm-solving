n = int(input())
array = list(map(int, input().split()))
result = []

for x in range(n):
    result.append((x+1)*array[x]-sum(result[:x]))

print(' '.join([str(n) for n in result]))
