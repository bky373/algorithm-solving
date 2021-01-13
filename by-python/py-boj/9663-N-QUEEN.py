# PyPy로 통과했고,
# Python3는 시간 초과 (찾아보니 답을 미리 구한 배열 제출 말고는 해결책이 없는 듯 ㅠㅠ)
def is_valid(nth):
    # 여기서 nth는 row의 n번째를 의미한다.
    for prev in range(nth):
        # row[x] 는 x번째 행의 col을 가리킨다.
        if row[nth] == row[prev]: return False  # 수직 체크
        if abs(row[nth] - row[prev]) == nth - prev: return False  # 대각선 체크
    return True


def dfs(nth):
    global res
    if nth == n:
        res += 1

    else:
        for cur_col in range(n):
            row[nth] = cur_col
            if is_valid(nth):  # 어차피 row는 사용가능하므로 굳이 매개변수로 안 넣어주고, nth만 넣어줌)
                dfs(nth + 1)


if __name__ == '__main__':
    n = int(input())
    row = [0] * n
    res = 0
    dfs(0)

    print(res)
