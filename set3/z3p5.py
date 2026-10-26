def make_ruler(x: int):
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
