def factorial(n):
    a = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        a *= i
    return a


print([factorial(i) for i in range(10)])
