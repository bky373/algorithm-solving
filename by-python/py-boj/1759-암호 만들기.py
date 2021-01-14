import re
from itertools import combinations


# 방법 1
# 따끈따끈하게 배운 정규식을 사용해보았다 :)
def is_valid(code):
    s_code = ''.join(code)
    if len(re.findall('[aeiou]', s_code)) < 1: return False
    if len(re.findall('[bcdfghjklmnpqrstvwxyz]', s_code)) < 2: return False
    return True


def dfs(code):
    if len(code) == l:
        if is_valid(code):
            print(''.join(code))
            return

    for i in range(c):
        if len(code) == 0:
            dfs(code + [arr[i]])
        elif code[-1] < arr[i]:
            dfs(code + [arr[i]])


# 방법 2
# itertools의 combinations를 사용해보았다.
def second():
    vowels = 'aeiou'

    for code in combinations(arr, l):
        cnt = 0
        for v in vowels:
            if v in code:
                cnt += 1

        if 1 <= cnt <= l - 2:
            print(''.join(code))


if __name__ == '__main__':
    l, c = map(int, input().split())
    arr = input().split()
    arr.sort()

    # dfs([])
    second()
