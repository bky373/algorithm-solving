def main():
    n = int(input())

    result = 0
    for i in range(1, n + 1):
        result += i * (n//i)
    print(result)


if __name__ == '__main__':
    main()
