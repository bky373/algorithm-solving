# PyPy3로 통과, Python3로는 시간 초과
# 방법 1
# 이중 for문 사용
# 시간 복잡도 O(N^2)
import sys

input = sys.stdin.readline


def solution(arr):
    S = [0] * (n + 1)

    for i in range(1, n + 1):
        # S[i] = S[i-1] + A[i]와 같은데,
        # 여기서 S[0]을 0으로 추가했으니 다음 식을 이용한다
        S[i] = S[i - 1] + arr[i - 1]

    count = 0
    for j in range(1, n + 1):
        for i in range(j, 0, -1):
            # A[i]..A[j]까지의 합 = S[j] - S[i - 1]
            if S[j] - S[i - 1] == m:
                count += 1
    return count


# 방법 2
# 두 개의 포인터 lo, hi 사용
# 시간 복잡도 O(N)
# 참고 : https://suri78.tistory.com/164
def solution_with_two_pointer(arr):
    cnt = 0
    lo, hi = 0, 1
    result = arr[lo]

    while lo < n:
        # 일치할 경우
        if result == m:
            cnt += 1
            result -= arr[lo]
            lo += 1

        # 종료 조건
        # 1) hi == n &&
        # 2-1) result > m 이더라도, lo를 높여볼 여지가 있기 때문에 종료 x
        # 2-2) result < m 이면, lo를 낮춰야 하는데
        # 그런 경우는 이미 해봤기 때문에 종료해도 된다.
        if hi == n and result < m:
            break

        # result < m 이면, lo는 그대로 hi를 높인다
        # result > m 이면, hi는 그대로 lo를 높인다
        elif result < m:
            result += arr[hi]
            hi += 1
        elif result > m:
            result -= arr[lo]
            lo += 1
    return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(solution(arr))
    print(solution_with_two_pointer(arr))
