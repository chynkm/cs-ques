# Complexity is O(m*n)
def arrayManipulation(n, queries):
    l = [0] * n
    for i in queries:
        for j in range(i[0]-1, i[1]):
            l[j] = l[j] + i[2]

    return max(l)


def arrayManipulation1(n, queries):
    l = [0] * n
    max_val = tot = 0

    for i in queries:
        l[i[0]-1] += i[2]
        if i[1] < len(l):
            l[i[1]] -= i[2]

    for i in l:
        tot += i
        if tot > max_val:
            max_val = tot

    return max_val


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

print(arrayManipulation1(n, queries))

# Ref: https://youtu.be/hDhf04AJIRs
