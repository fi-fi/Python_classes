# ---------------------- PYTHON-----------------------
# Set 3
# Author: Filip Kowalski
#
# Problem 6


def makedrawing(x, y):
    """This function displays a drawing composed
    of rectangles, of a given dimensions x and y."""
    cross = "+"
    verticalbar = "|"

    for i in range(x):
        cross += "---+"
        verticalbar += "{:>4}".format("|")
    for i in range(y):
        print(cross)
        print(verticalbar)
    print(cross)


makedrawing(4, 2)
