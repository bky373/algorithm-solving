""" 1번: 나의 풀이 (단순 구현) """
def solution(arr1, arr2):
    ans = [0] * len(arr1)
    for i in range(len(arr1)):
        tmp = []
        ans[i] = tmp
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
    return ans




""" 2번: 나의 풀이 (zip 1번 사용) """
def solution2(arr1, arr2):
    ans = []
    for a1, a2 in zip(arr1, arr2):
        x = 0
        tmp = [0] * len(a1)
        for _ in range(len(a2)):
            tmp[x] = a1[x] + a2[x]
            x += 1
        ans.append(tmp)
    return ans




""" 3번: 다른 사람의 풀이 (zip 2번 사용) """
def solution3(arr1, arr2):
    return [[c + d for c, d in zip(a,b)] for a,b in zip(arr1, arr2)]




""" 4번: 다른 사람의 풀이 (배열 재활용) """
def solution4(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1




""" 5번: 다른 사람의 풀이 (zip 두 번, 포인터 활용) """
def solution5(arr1, arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]
