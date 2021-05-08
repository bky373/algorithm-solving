data = input()
num = [int(s) for s in data]

num.sort(reverse=True)
print(''.join([str(n) for n in num]))
