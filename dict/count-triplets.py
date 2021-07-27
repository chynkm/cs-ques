# Numbers should be of the following format
# [n/r, n%r,  n*r] where r is the common ratio i.e.
# [1, 4, 16] Here, n = 4 and r = 4 resulting in
# [1, 0, 4]
# https://youtu.be/KZ8k9-22JmQ

from collections import Counter


def countTriplets(arr, r):
    before = {}
    after = Counter(arr)
    count = 0
    for i in arr:
        after[i] -= 1
        if i//r in before and i % r == 0 and i*r in after:
            count += before[i//r]*after[i*r]

        if i in before:
            before[i] += 1
        else:
            before[i] = 1

    return count


nums = {
    2: [1, 2, 2, 4],
    3: [1, 3, 9, 9, 27, 81],
    4: [1, 4, 16, 64],
    5: [1, 5, 5, 25, 125]
}

for k, v in nums.items():
    print(countTriplets(v, k))
