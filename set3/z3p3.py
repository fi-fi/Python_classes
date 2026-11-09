# ---------------------- PYTHON-----------------------
# Set 3
# Author: Filip Kowalski
#
# Problem 3


def nondiv_by_3_v1(n):
    """Function returns natural numbers less
    than n divisible by 3. Implemented through for loop"""
    for i in range(n + 1):
        if not i % 3 == 0:
            print(f"{i}\n")


def nondiv_by_3_v2(n):
    """Function returns natural numbers less
    than n divisible by 3. Implemented through while loop"""
    i = 0
    while i in range(n + 1):
        if i % 3 != 0:
            print("%2d\n" % i)
        i += 1
