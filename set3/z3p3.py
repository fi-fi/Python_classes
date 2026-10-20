# -----------------------PROBLEM 3----------------------


def nondiv_by_3_v1(n):
    for i in range(n + 1):
        if not i % 3 == 0:
            print(f"{i}\n")


def nondiv_by_3_v2(n):
    while (i := range(n + 1)) % 3 != 0:
        print(i)


nondiv_by_3_v1(30)
nondiv_by_3_v2(30)
