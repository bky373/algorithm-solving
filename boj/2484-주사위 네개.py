""" 1번: 내가 작성한 코드 """
n = int(input())

max_prize = 0
for _ in range(n):
    nums = [0 for _ in range(7)]
    for x in map(int, input().split()):
        nums[x] += 1 

    prize = 0
    for x in range(7):
        if nums[x] == 4:
            prize = 50_000 + x * 5_000
            break
        elif nums[x] == 3:
            prize = 10_000 + x * 1_000
            break
        elif nums[x] == 2:
            if 1 in nums:
                prize = 1_000 + x * 100
                break
            for y in range(7):
                if nums[y] == 2 and y != x:
                    prize = 2_000 + (x+y) * 500
                    break
    if not prize:
        for y in range(6, -1, -1):
            if nums[y] == 1:
                prize = y * 100
                break

    max_prize = max(max_prize, prize)
print(max_prize)




""" 2번: 1번 성공 후 참고한 코드 """
def money():
    lst = sorted(list(map(int, input().split())))
    if len(set(lst)) == 1:
        return lst[0] * 5000 + 50000
    if len(set(lst)) == 2:
        if lst[1] == lst[2]:
            return lst[1] * 1000 + 10000
        else:
            return (lst[1] + lst[2]) * 500 + 2000
    for i in range(3):
        if lst[i] == lst[i+1]:
            return lst[i] * 100 + 1000
    return lst[-1] * 100

N = int(input())
print(money() for i in range(N))
