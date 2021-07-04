#!/bin/python3

# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1,2,1,2,1,3,2]

# There is one pair of color  and one of color . There are three
# odd socks left, one of each color. The number of pairs is .


def sockMerchant(n, ar):
    sock_count = {}
    pairs = 0
    for i in ar:
        if i in sock_count:
            pairs += 1
            del sock_count[i]
        else:
            sock_count[i] = True

    return pairs


def sockMerchant1(n, ar):
    sock_count = {}
    for i in ar:
        sock_count[i] = (sock_count[i] + 1) if i in sock_count else 1

    pairs = 0
    for i in sock_count.values():
        pairs = pairs + (i // 2)

    return pairs


n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

sockMerchant(n, ar)
