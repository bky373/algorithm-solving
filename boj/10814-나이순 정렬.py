""" 1. 내가 작성한 코드 (dictionary 이용) """
n = int(input())
members = dict()

for x in range(1, 201):
    members[x] = []    

for x in range(n):
    age, name = input().split()
    members[int(age)].append(name)

for k, names in members.items():
    for name in names:
        print(k, name)

""" 2. 1번 통과 후 참고한 코드 (튜플, 기본 정렬 library(sorted) 이용) """
n = int(input())

array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array = sorted(array, key=lambda x: x[0])

for x in array:
    print(x[0], x[1])
    