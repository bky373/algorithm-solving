def main():
    T = int(input())
    MX = 100
    triangle = [1] * MX
    triangle[3] = triangle[4] = 2
    for i in range(5, MX):
        triangle[i] = triangle[i - 5] + triangle[i - 1]

    for _ in range(T):
        n = int(input())
        print(triangle[n - 1])


if __name__ == '__main__':
    main()
