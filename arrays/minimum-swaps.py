def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                swaps += 1
                arr[i], arr[j] = arr[j], arr[i]
    return swaps


a = [2, 3, 4, 1, 5]
a = [1, 3, 5, 2, 4, 6, 7]
a = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(a))
