import heapq


def solve(arr):
    pq = []
    for i in range(n):
        heapq.heappush(pq, arr[i][1])
        if len(pq) > arr[i][0]:
            heapq.heappop(pq)
    return sum(pq)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort()

    print(solve(arr))
