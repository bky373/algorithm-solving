def solution(base, e, divisor):
    result = 1

    while e:
        if e & 1:  # e가 홀수면 true, 짝수면 false
            result = result * base % divisor
        e //= 2
        base = base * base % divisor
    return result


def solution_rec(base, e, divisor):
    if e == 0: return 1

    k = solution_rec(base, e // 2, divisor)
    result = k * k % divisor

    if e % 2:
        return base * result % divisor
    else:
        return result


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(solution(a, b, c))
    # print(solution_rec(a, b, c))
