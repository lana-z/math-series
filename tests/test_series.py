from math_series.series import fibonacci

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 1
    assert actual == expected

def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 3
    assert actual == expected