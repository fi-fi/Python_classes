def sum_seq(sequence):
    if not any([isinstance(i, (tuple, list)) for i in sequence]):
        return sum(sequence)
    else:
        summed = [
            sum_seq(i) if isinstance(i, (list, tuple)) else 0 if i == None else i
            for i in sequence
        ]
        return sum_seq(summed)


assert sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == sum(
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
)
