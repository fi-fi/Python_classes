# -----------------------PROBLEM 3----------------------


def nondiv_by_3_v1(n):
    for i in range(n + 1):
        if not i % 3 == 0:
            print(f"{i}\n")


def nondiv_by_3_v2(n):
    i = 0
    while i in range(n + 1):
        if i % 3 != 0:
            print("%2d\n" % i)
        i += 1


assert (nondiv_by_3_v1(6)) == "1\n2\n4\n5\n"
