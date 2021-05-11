def hanoi(N, start, destination, via, result):
    if N <= 1:
        result.append((start, destination))
        return 1

    count = 0
    count += hanoi(N - 1, start, via, destination, result)
    count += 1
    result.append((start, destination))

    count += hanoi(N - 1, via, destination, start, result)

    return count


if __name__ == '__main__':
    N = int(input())

    if N > 20:
        print(2 ** N - 1)
        exit()

    start = 1
    via = 2
    destination = 3

    result = []
    total_count = hanoi(N, start, destination, via, result)

    print(total_count)
    for from_pos, to_pos in result:
        print(from_pos, to_pos)
