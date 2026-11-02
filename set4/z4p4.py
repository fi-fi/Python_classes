def fibonacci(n):
    a = 1
    b = 1
    if n == 0 | n == 1:
        return 1
    for i in range(1, n):
        a, b = a + b, a
    return a


print([fibonacci(n) for n in range(10)])
