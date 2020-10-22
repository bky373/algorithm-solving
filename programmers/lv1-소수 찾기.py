""" 1번: 나의 풀이 """
def solution(n):
    return prime_list(n)

def prime_list(n):
    prime_nums = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m+1):
        if prime_nums[i]:
            for j in range(i+i, n+1, i):
                prime_nums[j] = False

    return len([i for i in range(2, n+1) if prime_nums[i]])




""" 2번: 다른 사람의 풀이(차집합 이용) """
def solution2(n):
    nums = set(range(2, n+1))

    for x in range(2, n+1):
        if x in nums:
            nums -= set(range(2*x, n+1, x))
    return len(nums)
