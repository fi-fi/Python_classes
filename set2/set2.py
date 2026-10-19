# -----------------------Python classes----------------------
# SET 2
# Author: Filip Kowalski
# Here i present the solutions of tasks from 2nd set


line = "afjdf\n fafsaf\t fsadfGvRgalg,.dfas\naf. uGvR"
word = "Hello"
L = [2, 3, 10, 4, 2, 357, 40, 36, 3, 2, 5]
number = 325053050052


def my_wordcount(string: str):  # 2.10
    """This function counts words in given string."""
    l = string.split()
    return len(l)


def my_underscore(string: str):  # 2.11
    """This function separates characters with underscores."""
    c = ""
    l = string.strip()
    for i in range(len(l) - 1):
        c += l[i]
        c += "_"
    c += l[-1]
    return c


def my_firststrings(string: str):  # 2.12
    """Returning the string composed of first
    strings of each word."""
    c = ""
    l = string.split()
    for i in l:
        c += i[0]
    return c


def my_laststrings(string: str):  # 2.12
    """This function returns the string composed
    of last strings of each word."""
    c = ""
    l = string.split()
    for i in l:
        c += i[-1]
    return c


def wordsum(string: str):  # 2.13
    """Returning the sum of lengths of words
    of a given string."""
    l = string.split()
    l2 = [len(i) for i in l]  # list comprehension of
    return sum(l2)  # consecutive wordlengths


def my_characteristics(string: str):  # 2.14
    """Returns a tuple of the longest word with its
    length from a given string."""
    l = string.split()
    return max(l, key=len), len(max(l, key=len))


def my_converted(list):  # 2.15
    """Given a list, returns a string with consecutive
    elements from the list."""
    s = ""
    for i in list:
        s += str(i)
    return s


def my_guido(string: str):  # 2.16
    """Replaces 'GvR' string with 'Guido van Rossum'"""
    while "GvR" in string:
        for i in range(len(string)):
            if string[i : i + 3] == "GvR":
                string = string[:i] + "Guido van Rossum" + string[i + 3 :]
    return string


def my_sorted(string: str):  # 2.17
    """Returns a tuple of a sorted lists of words, first is
    sorted lexicographically, and the second- by length."""
    return sorted(string.split()), sorted(string.split(), key=len)


def my_zeros(n: int):  # 2.18
    """This function returns number of
    ocurrences of 0 in given int."""
    s = str(n)
    c = 0
    for i in s:
        if i == "0":
            c += 1
    return c


def my_adjusted(l):  # 2.19
    """Given a list of 1,2,3- digit numbers, returns a string
    of those numbers filled with zeros to make them 3- digit."""
    s = ""
    for i in l:
        s += str(i).zfill(3) + "\n"
    return s


print(f"{my_wordcount(line)}\n")
print(f"{my_underscore(word)}\n")
print(f"{my_firststrings(line)}\n")
print(f"{my_laststrings(line)}\n")
print(f"{wordsum(line)}\n")
print(f"{my_characteristics(line)}\n")
print(f"{my_converted(L)}\n")
print(f"{my_guido(line)}\n")
print(f"{my_sorted(line)}\n")
print(f"{my_zeros(number)}\n")
print(my_adjusted(L))
