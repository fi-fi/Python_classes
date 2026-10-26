def my_cube():
    """This function returns inserted number cubed,
    and is protected from inserting strings"""
    while True:
        x = input("Please, enter real number:\
        (enter 'stop' to quit)")
        if x == "stop":
            break
        try:
            x = float(x)
        except ValueError:
            print("This is not a real number!\n \
                Please enter proper number.")
        else:
            print("{0:.3f}".format(x**2))


if __name__ == "__main__":
    my_cube()
