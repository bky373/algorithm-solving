data = list(map(int, input().split(' ')))

ascending = True
descending = True

for x in range(1, 8):
    if data[x-1] < data[x]:
        descending = False
    elif data[x] < data[x-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
