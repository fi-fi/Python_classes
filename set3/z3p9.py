def seq_sum(l):
    return [sum(a) for a in l]


l1 = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
l2 = [[], [1, 2], (9, 8, 7)]

assert (seq_sum(l1)) == [0, 4, 3, 7, 18]
assert (seq_sum(l2)) == [0, 3, 24]
