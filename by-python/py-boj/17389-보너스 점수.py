n = int(input())
s = input()
total, bonus = 0, 0
o, x = 'O', 'X'

for i in range(n):
    if s[i] == o:
        total += (i+1) + bonus
        bonus += 1
    else:
        bonus = 0

print(total)
