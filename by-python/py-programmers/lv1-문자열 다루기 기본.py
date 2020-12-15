def solution(s):
    return len(s) in (4, 6) and s.isdigit()


if __name__ == '__main__':
    print(solution(input()))
