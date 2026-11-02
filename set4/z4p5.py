def revert(L, left, right):
    Lrev = L[left : right + 1]
    print(Lrev)
    for i in range(0, right + 1 - left):
        L[left + i] = Lrev[right - left - i]
    return


L = [2, 8, 6, 45, 44, 6]
revert(L, 1, 5)
print(L)
