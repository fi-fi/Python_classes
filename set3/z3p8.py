def findcommon(a, b):
    sa = set(a)
    sb = set(b)
    if len(sa) < len(sb):
        print([i for i in sb if i in sa])
    else:
        print([i for i in sa if i in sb])


def merge(a, b):
    sa = set(a)
    sb = set(b)
    l1 = [i for i in sa]
    l2 = [i for i in sb if i not in sa]
    print(l1 + l2)


a = [1, 1, 2, 3, 23, 3, 4, 250, 300]
b = [3, 4, 1, 8, 8, 23, 100, 250]


findcommon(a, b)
merge(a, b)
