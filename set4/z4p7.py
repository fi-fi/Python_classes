def my_flatten(sequence):
    if all([not isinstance(i, (tuple, list)) for i in sequence]):
        return sequence
    else:
        nlist = []
        for i in sequence:
            if isinstance(i, (list, tuple)):
                nlist = [*nlist, *i]
            else:
                nlist.append(i)
        return my_flatten(nlist)


assert my_flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]
