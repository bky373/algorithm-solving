sold_books = dict()
bestseller = ""
n = int(input())

for _ in range(n):
    max = 0
    title = input() 
    if title not in sold_books:
        sold_books[title] = 1
    else:
        sold_books[title] += 1
    
    for k, v in sold_books.items():
        if v > max:
            max = v
            bestseller = k
        elif v == max:
            if bestseller > k:
                bestseller = k

print(bestseller)
