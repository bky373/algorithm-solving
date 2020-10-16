a, b, c = map(int, input().split())
nums = set([a, b, c])

if len(nums) == 1:
    print(10_000 + a*1_000)
elif len(nums) == 3:
    print(max(nums)*100)
else:
    if a == b or a == c:
        print(1_000 + a*100)
    else:
        print(1_000 + b*100)
