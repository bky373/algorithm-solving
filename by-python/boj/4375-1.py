def solution(n):
    cnt = 1
    num = 1
    while True:
        if num % n == 0:
            return cnt
        num = num * 10 + 1
        cnt += 1


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
        except EOFError:
            exit(0)

        print(solution(n))
