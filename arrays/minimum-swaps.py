def minimumSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
            swaps += 1

    return swaps


a = [4, 3, 1, 2]
a = [2, 3, 4, 1, 5]
a = [1, 3, 5, 2, 4, 6, 7]
a = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(a))
