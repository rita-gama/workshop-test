from solution import add, subtract, multiply

def test_add():
    assert add(1, 1) == 2

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6