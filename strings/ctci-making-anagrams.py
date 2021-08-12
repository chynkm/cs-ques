from collections import Counter


def makeAnagram1(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    delete_count = 0
    for element in set(a + b):
        delete_count += abs(counter_a[element] - counter_b[element])

    return delete_count


def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    c = counter_a - counter_b
    d = counter_b - counter_a
    return sum((c + d).values())


a = "cde"
b = "dcf"
a = "cde"
b = "abc"
print(makeAnagram(a, b))
