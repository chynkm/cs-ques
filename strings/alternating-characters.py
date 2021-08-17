def alternatingCharacters(s):
    count = 0
    s = list(s)
    for i in range(1, len(s)):
        if (s[i] == s[i-1]):
            count += 1

    return count


strings = [
    'AABAAB',
    'AAAA',
    'BBBBB',
    'ABABABAB',
    'BABABA',
    'AAABBB',
]

for s in strings:
    print(alternatingCharacters(s))
