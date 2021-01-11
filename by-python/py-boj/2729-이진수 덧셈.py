import sys

input = sys.stdin.readline


# 방법 1
# 직접 구현 (속도는 내장함수 구현과 큰 차이 없음)
def solution():
    n = int(input())
    for _ in range(n):
        a, b = input().split()
        c = [0] * (max(len(a), len(b)) + 1)
        a = a.zfill(len(c))
        b = b.zfill(len(c))

        forward = 0
        i = len(c) - 1

        while i >= 0:
            if forward:
                if a[i] == '1' and b[i] == '1':
                    c[i] = 1
                elif a[i] == '0' and b[i] == '0':
                    c[i] = 1
                    forward = 0
                else:
                    c[i] = 0
            elif a[i] == '1' and b[i] == '1':
                forward = 1
                c[i] = 0
            else:
                c[i] = int(a[i]) if a[i] == '1' else int(b[i])
            i -= 1

        if all(x == 0 for x in c):
            print(0)
        else:
            print(''.join((map(str, c))).lstrip('0'))


# 방법 2
# 내장함수 활용
def easy_solution():
    n = int(input())
    for _ in range(n):
        result = sum(map(lambda k: int(k, 2), input().split()))
        print(bin(result)[2:])


if __name__ == '__main__':
    # solution()
    easy_solution()
