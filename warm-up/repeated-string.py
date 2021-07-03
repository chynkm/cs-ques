#!/bin/python3

# There is a string, s, of lowercase English letters that is repeated
# infinitely many times. Given an integer, a, find and print the number
# of letter a's in the first n letters of the infinite string.
#
# s = 'abcac'
# n = 10
# The substring we consider is abcacabcac, the first 10 characters of
# the infinite string. There are  occurrences of a in the substring.


def repeatedString(s, n):
    total = ((n // len(s)) * s.count('a')) + s[0:(n % len(s))].count('a')
    print(total)


repeatedString('aba', 10)
repeatedString('a', 1000000000000)
