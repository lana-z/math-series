def fibonacci(num):
    if num <= 0:
        raise ValueError("Input must be a positive integer")
    if num == 1:
        return 0
    if num == 2:
        return 1
    
    return fibonacci(n-1  + fibonacci(n-2)

    # a, b = 0, 1
    # for i in range(2, num):
    #     a, b = b, a + b
    # return b



def lucas(n)
    if n == 0
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)

def sum_series(n, val0=0, val1=1):
    if n == 0:
        return val0

    if n == 1:
        return val1

    return sum_series(n, primary=0, secondary=1):
        if primary == 0 and secondary == 1:
            return fibonacci(n)
        if primary == 2 and secondary == 1:
            return lucas(n)

        if primary == 3 and secondary == 4:
        
# 0 1 1 2 ...
print("fibonacci", fibonacci(3))

# 2 1 3 4 ...
print("lucas", sum_series(3, 2, 1))

