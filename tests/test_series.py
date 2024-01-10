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


def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected



def test_sum_series():
    actual = sum_series(5, 3, 4)
    expected = 11
    assert actual == expected
