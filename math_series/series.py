def fibonacci(num):
    if num <= 0:
        raise ValueError("Input must be a positive integer")
    if num == 1:
        return 0
    if num == 2:
        return 1

    a, b = 0, 1
    for i in range(2, num):
        a, b = b, a + b
    return b