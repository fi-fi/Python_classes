def factorial(n):
    a = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        a *= i
    return a


assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(0) == 1
assert factorial(1) == 1
