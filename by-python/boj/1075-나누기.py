N = input()
F = int(input())

new_num = N[:-2] + '00'
tmp = int(new_num)
while True:
    if tmp % F == 0:
        break
    tmp += 1

print(str(tmp)[-2:])
