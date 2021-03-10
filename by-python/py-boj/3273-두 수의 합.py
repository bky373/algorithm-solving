n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

numbers.sort()

lo, hi = 0, len(numbers) - 1

answer = 0
while lo < hi:
    sum_two = numbers[lo] + numbers[hi]
    if sum_two == target:
        answer += 1
        lo += 1

    elif sum_two < target:
        lo += 1
    elif sum_two > target:
        hi -= 1

print(answer)
