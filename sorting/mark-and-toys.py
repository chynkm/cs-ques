def maximumToys(prices, k):
    items = 0
    if len(prices) == 0 or k == 0:
        return items

    prices.sort()
    for i in prices:
        if i < k:
            items += 1
            k -= i

    return items


print(maximumToys([4, 3, 2, 1], 7))
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
# maximumToys([4, 3, 2, 1], 7)
