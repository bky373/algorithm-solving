# from collections import deque
#
#
# # 방법 1
# def main():
#     n, k = map(int, input().split())
#     q = deque(map(str, range(1, n + 1)))
#
#     cnt = 0
#     ans = '<'
#     while cnt < n - 1:
#         i = 0
#         while i < k - 1:
#             q.append(q.popleft())
#             i += 1
#         if q: ans += f'{q.popleft()}, '
#         cnt += 1
#     ans += f'{q[0]}>'
#     print(ans)


# 방법 2
def main():
    n, k = map(int, input().split())
    arr = list(map(str, range(1, n + 1)))
    ans = '<'
    cnt = 0
    i = 0

    while cnt < n - 1:
        kth = (i + (k - 1)) % len(arr)
        if arr: ans += f'{arr[kth]}, '
        del arr[kth]
        i = kth
        cnt += 1

    ans += f'{arr[0]}>'
    print(ans)


if __name__ == '__main__':
    main()
