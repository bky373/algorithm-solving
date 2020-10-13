""" 1번: 내가 작성한 코드(max 이용) """
trophies = [] 
left, right = 1, 1

n = int(input())

for _ in range(n):
    trophies.append(int(input()))

max_before, highest = 0, max(trophies)
for x in range(n):
    if max_before < trophies[x] and trophies[x] < highest:
        left += 1
    max_before = max(trophies[:x+1])

max_before, highest = 0, max(trophies)
trophies = trophies[::-1]
for x in range(n):
    if max_before < trophies[x] and trophies[x] < highest:
        right += 1
    max_before = max(trophies[:x+1])
print(left, right, sep='\n')



""" 2번: 1번 성공 후 참고한 코드(오름차순 정렬 활용) """
def ascending(array):
    now = array[0]
    result = 1
    for x in range(1, len(array)):
        if now < array[x]:
            result += 1
            now = array[x]
    return result

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))
