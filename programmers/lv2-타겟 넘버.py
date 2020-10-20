""" 1번: 내가 작성한 풀이 """
from collections import deque

def solution(numbers, target):
    total = sum(numbers)
    n = len(numbers)
    operators_list = deque()
    answer = 0

    get_operators([], operators_list, n)

    for operators in operators_list:
        res = total
        for i in range(n):
            if operators[i] == '-':
                res -= 2 * numbers[i]
        if res == target:
            answer += 1
    return answer

def get_operators(ops, operators_list, n):
    if len(ops) == n:
        operators_list.append(ops[:])
        return

    ops.append('+')
    get_operators(ops, operators_list, n)
    ops.pop()

    ops.append('-')
    get_operators(ops, operators_list, n)
    ops.pop()



""" 2번: 1번 성공 후 참고한 풀이 """
def dfs(nums, i, n, target):
    ret = 0
    if i == len(nums):
        if n == target: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], target)
    ret += dfs(nums, i+1, n-nums[i], target)
    return ret

def solution2(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
