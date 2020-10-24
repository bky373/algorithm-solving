""" 1번: 나의 풀이 """
def solution(n, arr1, arr2):
    secret_map = list(map(lambda x: format(x[0]|x[1], 'b'), zip(arr1, arr2)))
    answer = []
    for s in secret_map:
            tmp = ''
            while len(s) < n:
                s = '0'+s
            for b in s:
                if b == '1':
                    tmp += '#'
                else:
                    tmp += ' '
            answer.append(tmp)
    return answer





""" 2번: 다른 사람의 풀이(rjust, replace 활용) """
def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = str(bin(arr1[i]|arr2[i])[2:]).rjust(n, '0').replace('1','#').replace('0',' ')
        answer.append(a)
    return answer





""" 3번: 다른 사람의 풀이(zfill 활용) """
solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

print("{0:d}".format(2))
print("{0:b}".format(2.0))
print("{0:o}".format(42))
print("{0:x}".format(42))