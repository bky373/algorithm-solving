def solution(num):
    i = 0
    while i < 500:
        if num == 1:
            return i
        if num % 2:
            num = num*3 + 1
        else:
            num //= 2
        i += 1
    return -1
