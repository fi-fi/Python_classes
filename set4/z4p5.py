def revert(L, left, right):
    Lrev = L[left : right + 1]
    for i in range(0, right + 1 - left):
        L[left + i] = Lrev[right - left - i]
    return L


assert revert([1, 4, 5, 6, 3], 2, 4) == [1, 4, 3, 6, 5]
