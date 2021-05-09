""" 1번: 나의 풀이 """
def solution(arr):
    ans = [arr[0]]
    k = 0
    for x in range(len(arr)):
        if arr[x] == ans[k]:
            continue
        ans.append(arr[x])
        k += 1
    return ans




""" 2번: 다른 사람의 풀이 """
def solution2(arr):
    ans = []
    for a in arr:
        if ans[-1:] == [a]:
            continue
        ans.append(a)
    return ans
    