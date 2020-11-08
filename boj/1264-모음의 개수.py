vowels = ['a','e','i','o','u','A','E','I','O','U']
while True:
    count = 0
    S = input()
    if S == '#':
        break
    for s in S:
        if s in vowels:
            count += 1
    print(count)
    