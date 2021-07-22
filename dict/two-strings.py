def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return 'YES'

    return 'NO'


s = [
    ['hello', 'world'],
    ['hi', 'world'],
]

for i in s:
    print(twoStrings(i[0], i[1]))
