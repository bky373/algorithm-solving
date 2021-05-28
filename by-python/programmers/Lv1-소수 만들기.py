def is_prime(num):
    for i in range(2, int(num **.5 ) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                num = nums[i] + nums[j] + nums[k]
                if is_prime(num):
                    answer += 1
    
    return answer
