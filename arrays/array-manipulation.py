# Complexity is O(m*n)
def arrayManipulation(n, queries):
    l = [0] * n
    for i in queries:
        for j in range(i[0]-1, i[1]):
            l[j] = l[j] + i[2]

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
