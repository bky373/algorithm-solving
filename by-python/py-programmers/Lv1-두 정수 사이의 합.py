def solution(a, b):
    if a == b: return a
    return sum(range(min(a, b), max(a, b) + 1))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solution(a, b))
