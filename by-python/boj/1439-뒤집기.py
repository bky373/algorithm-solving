def solve(data):
    cnts = [0, 0]

    if data[0] == '0':
        cnts[1] += 1
    else:
        cnts[0] += 1

    for i in range(len(data) - 1):
        if data[i] != data[i + 1]:
            if data[i + 1] == '0':
                cnts[1] += 1
            else:
                cnts[0] += 1

    return min(cnts)


if __name__ == '__main__':
    data = input()
    print(solve(data))
