""" 1번: 나의 풀이(2차원적 접근) """
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
           print('*', end='')
    print()
    


""" 2번: 나의 풀이(1차원적 접근) """
a, b = map(int, input().strip().split(' '))

for x in range(1, a*b+1):
    if x % a == 0:
        print('*')
    else:
        print('*', end='')



""" 3번: 1,2번 성공 후 참고한 풀이(O(1)) """
a, b = map(int, input().strip().split(' '))
print(('*' * a + '\n') * b)
