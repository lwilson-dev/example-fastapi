from app.calculations import add, subtract, multiply, divide
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (9, 4, 13),
    (3, 4, 7),
    (10, 2, 12)
])
def test_add(num1, num2, expected):
    print("Testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    print("Testing subtract function")
    assert subtract(9, 4) == 5

def test_multiply():
    print("Testing multiply function")
    assert multiply(3, 4) == 12

def test_divide():
    print("Testing divide function")
    assert divide(10, 2) == 5