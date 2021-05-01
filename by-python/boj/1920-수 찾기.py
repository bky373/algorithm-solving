n = int(input())
base_nums = set(map(int, input().split(' ')))
m = int(input())
compare_nums = list(map(int, input().split(' ')))

for n in compare_nums:
    if n not in base_nums:
        print(0)
    else:
        print(1)
