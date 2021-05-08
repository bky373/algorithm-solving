def solve(arr):
    maximum = arr[2] * arr[3] * arr[4]
    result = 0
    for k in range(arr[0], maximum + 1):
        count = 0
        for i in range(5):
            if k % arr[i] == 0 and k >= arr[i]:
                count += 1
            if count >= 3:
                result = k
                break
        else:
            continue
        break
    return result


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    arr.sort()
    print(solve(arr))
