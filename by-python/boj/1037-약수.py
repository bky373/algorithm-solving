def solve(nums):
    nums.sort()
    sz = len(nums)
    if sz % 2 == 0:
        return nums[0] * nums[-1]
    else:
        mid = len(nums)//2
        return nums[mid] ** 2


if __name__ == '__main__':
    cnt = int(input())
    nums = list(map(int, input().split()))

    print(solve(nums))
