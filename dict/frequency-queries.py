def freqQuery(queries):
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
