def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1)  + fibonacci(n-2)

def lucas(n):
    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)

def sum_series(n, first_position=0, second_position=1):
    if n == 0:
        return first_position

    if n == 1:
        return second_position

    return sum_series(n, first_position=0, second_position=1):
        if first_position == 0 and second_position == 1:
            return fibonacci(n) 
        if first_position == 2 and second_position == 1:
            return lucas(n)

        if first_position == 3 and second_position == 4:    
        
# 0 1 1 2 ...
print("fibonacci", fibonacci(3))

# 2 1 3 4 ...
print("lucas", sum_series(3))

