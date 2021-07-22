# len(s1) == len(s2)
# freq of each char in s1 = freq of each character in s2

# count = n(n-1)/2
# take substring and sort them before saving it to dictionary


def sherlockAndAnagrams(s):
    my_dict = {}
    for i in range(1, len(s)):
        a = 0
        b = a + i
        while b <= len(s):
            temp = ''.join(sorted(s[a:b]))
            my_dict[temp] = my_dict.get(temp, 0) + 1
            a += 1
            b += 1

    return calculateCount(my_dict)


def calculateCount(d):
    c = 0
    for k, v in d.items():
        c += v*(v-1)//2

    return c


strings = [
    'abba',
    'kkkk',
]

for string in strings:
    print(sherlockAndAnagrams(string))
