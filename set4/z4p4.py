def fibonacci(n):
    a = 1
    b = 1
    if n == 0 | n == 1:
        return 1
    for i in range(1, n):
        a, b = a + b, a
    return a


assert fibonacci(0) == 1
assert fibonacci(1) == 1
assert fibonacci(2) == 2
assert fibonacci(3) == 3
