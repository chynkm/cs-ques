from collections import Counter


def freqQuery1(queries):
    my_dict = {}
    output = []
    for k, v in queries:
        if k == 1:
            if v in my_dict:
                my_dict[v] += 1
            else:
                my_dict[v] = 1
        elif k == 2:
            if v in my_dict:
                my_dict[v] -= 1
                if my_dict[v] == 0:
                    del my_dict[v]
        else:
            r = int_freq(my_dict, v)
            output.append(r)

    return output


def int_freq(my_dict, v):
    for count in my_dict.values():
        if count == v:
            return 1
    return 0


def freqQuery2(queries):
    my_dict = {}
    output = []
    for k, v in queries:
        if k == 1:
            if v in my_dict:
                my_dict[v] += 1
            else:
                my_dict[v] = 1
        elif k == 2:
            if v in my_dict:
                my_dict[v] -= 1
                if my_dict[v] == 0:
                    del my_dict[v]
        else:
            if v in my_dict.values():
                output.append(1)
            else:
                output.append(0)

    return output


def freqQuery3(queries):
    my_dict = Counter()
    my_values_dict = Counter()
    output = []
    for k, v in queries:
        if k == 1:
            if my_values_dict[my_dict[v]] > 0:
                my_values_dict[my_dict[v]] -= 1

            my_dict[v] += 1
            my_values_dict[my_dict[v]] += 1

        elif k == 2:
            if my_dict[v] > 0:
                if my_values_dict[my_dict[v]] > 0:
                    my_values_dict[my_dict[v]] -= 1

                my_dict[v] -= 1
                if my_dict[v] > 0:
                    my_values_dict[my_dict[v]] += 1

        else:
            if my_values_dict[v] > 0:
                output.append(1)
            else:
                output.append(0)

    return output


def freqQuery(queries):
    my_dict = Counter()
    my_values_dict = Counter()
    output = []
    for k, v in queries:
        if k == 1:
            my_values_dict[my_dict[v]] -= 1
            my_dict[v] += 1
            my_values_dict[my_dict[v]] += 1

        elif k == 2:
            if my_dict[v] > 0:
                my_values_dict[my_dict[v]] -= 1
                my_dict[v] -= 1
                my_values_dict[my_dict[v]] += 1

        else:
            output.append(1 if my_values_dict[v] > 0 else 0)

    return output


queries = [
    [
        (1, 1),
        (2, 2),
        (3, 2),
        (1, 1),
        (1, 1),
        (2, 1),
        (3, 2),
    ],
    [
        (1, 5),
        (1, 6),
        (3, 2),
        (1, 10),
        (1, 10),
        (1, 6),
        (2, 5),
        (3, 2),
    ],
    [
        (3, 4),
        (2, 1003),
        (1, 16),
        (3, 1),
    ],
    [
        (1, 3),
        (2, 3),
        (3, 2),
        (1, 4),
        (1, 5),
        (1, 5),
        (1, 4),
        (3, 2),
        (2, 4),
        (3, 2),
    ]
]


for query in queries:
    print(freqQuery(query))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

#     ans = freqQuery(queries)

#     fptr.write('\n'.join(map(str, ans)))
#     fptr.write('\n')

#     fptr.close()
