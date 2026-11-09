# ---------------------- PYTHON-----------------------
# Set 3
# Author: Filip Kowalski
#
# Problem 5


def make_ruler(x: int):
    """This function displays a ruler of given
    length, up to 12."""
    if x > 12:
        print("Ruler is too long to be shown!")
        return
    miarka = "|"
    liczby = "0"

    for i in range(1, x + 1):
        miarka += "....|"
        liczby += "{:>5}".format(i)

    print(miarka)
    print(liczby)


make_ruler(6)
make_ruler(12)

assert (make_ruler(13)) == None
