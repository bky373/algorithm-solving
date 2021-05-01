def is_prime(n):
    if n == 1: return False

    k = int(n ** 0.5)
    for i in range(2, k + 1):
        if n % i == 0:
            return False
    else:
        return True


def solution(numbers):
    cnt = 0
    for n in numbers:
        if is_prime(n):
            cnt += 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    print(solution(numbers))
