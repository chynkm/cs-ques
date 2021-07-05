def minimumSwaps(arr):
    swaps = 0
    a = dict(enumerate(arr, 1))
    for k, v in a.items():
        if k != v:
            a[v], a[k] = v, a[v]
            swaps += 1

    return swaps


a = [2, 3, 4, 1, 5]
# a = [1, 3, 5, 2, 4, 6, 7]
# a = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(a))
