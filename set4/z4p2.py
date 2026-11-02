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

    return miarka + "\n" + liczby


def makedrawing(x, y):
    """This function displays a drawing composed
    of rectangles, of a given dimensions x and y."""
    cross = "+"
    verticalbar = "|"
    string = ""
    for i in range(x):
        cross += "---+"
        verticalbar += "{:>4}".format("|")

    for i in range(y):
        string += cross + "\n"
        string += verticalbar + "\n"
    return string + cross


assert make_ruler(15) == None
