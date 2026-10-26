def makedrawing(x, y):
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
