def revert(L, left, right):
    Lrev = L[left : right + 1]
    for i in range(0, right + 1 - left):
        L[left + i] = Lrev[right - left - i]
    return L


def revert_rec(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        revert_rec(L, left + 1, right - 1)
    return L


assert revert([1, 4, 5, 6, 3], 2, 4) == [1, 4, 3, 6, 5]
assert revert_rec([1, 4, 5, 6, 3], 2, 4) == [1, 4, 3, 6, 5]

assert revert([i for i in range(10)], 4, 7) == [0, 1, 2, 3, 7, 6, 5, 4, 8, 9]
assert revert_rec([i for i in range(10)], 4, 7) == [0, 1, 2, 3, 7, 6, 5, 4, 8, 9]
