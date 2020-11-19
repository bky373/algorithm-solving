def solution(numbers):
    n = len(numbers)
    ans = set()
    for i in range(n-1):
        for j in range(i+1, n):
            num = numbers[i] + numbers[j]
            if num not in ans:
                ans.add(num)
    return list(sorted(ans))
    