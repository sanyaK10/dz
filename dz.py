prices = [50, 120, 75, 200, 90, 130, 60]
total = sum(prices)
count_over_100 = 0
for price in prices:
    if price > 100:
        count_over_100 += 1

print("Список цін:", prices)
print("Загальна сума:", total)
print("Кількість товарів > 100 грн:", count_over_100)