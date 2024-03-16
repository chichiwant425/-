T = int(input())
for _ in range(T):
    m,n=map(int, input().split())
    shop_names = input().split()
    prices = []
    for _ in range(m):
        prices.append(list(map(float, input().split())))
    min_prices = []
    for i in range(n):
        min_price = min([prices[j][i] for j in range(m)])
        min_prices.append(min_price)
    book_count = [0] * m
    for i in range(m):
        for j in range(n):
            if prices[i][j] == min_prices[j]:
                book_count[i] += 1
    shop_books = zip(shop_names, book_count)
    sorted_shop_books = sorted(shop_books, key=lambda x: (-x[1], x[0]))
    for shop, book in sorted_shop_books:
        print(f"{shop} {book}")

