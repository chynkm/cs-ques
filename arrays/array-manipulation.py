def arrayManipulation(n, queries):
    l = [0] * n
    for i in queries:
        a = i[0] - 1
        b = i[1]
        k = i[2]
        for j in range(a, b):
            l[j] = l[j] + k

    return max(l)


n = 5
queries = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100],
]
n = 10

queries = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1],
]

print(arrayManipulation(n, queries))
