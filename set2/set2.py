line = "afjdf\n fafsaf\t fsadfGvRgalg,.dfas\naf. uGvR"
word = "Hello"
L = [2, 3, 10, 4, 2, 357, 40, 36, 3, 2, 5]


def my_wordcount(string: str):
    l = string.split()
    return len(l)


def my_underscore(string: str):
    c = ""
    l = string.strip()
    for i in range(len(l) - 1):
        c += l[i]
        c += "_"
    c += l[-1]
    return c


def my_laststrings(string: str):
    c = ""
    l = string.split()
    print(l)
    for i in l:
        c += i[-1]
    return c


def my_stringlength(string: str):
    l = string.split()
    l2 = [len(i) for i in l]
    return sum(l2)


def my_characteristics(string: str):
    l = string.split()
    print(sorted(l, key=len))
    return max(l, key=len), len(max(l, key=len))


def my_converted(list):
    s = ""
    for i in list:
        s += str(i)
    return s


def my_guido(string: str):
    while "GvR" in string:
        for i in range(len(string)):
            if string[i : i + 3] == "GvR":
                string = string[:i] + "Guido van Rossum" + string[i + 3 :]
    return string


def my_sorted(string: str):
    return sorted(string.split()), sorted(string.split(), key=len)


def my_adjusted(l):
    s = ""
    for i in l:
        s += str(i).zfill(3) + "\n"
    return s


print(word.split())
print(my_underscore(word))
print(my_laststrings(line))
print(my_stringlength(line))
print(my_characteristics(line))
print(my_converted(L))
print(my_guido(line))
print(my_sorted(line))
print(my_adjusted(L))
