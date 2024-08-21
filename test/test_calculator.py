from app.calculator import sum, subtract, multiply, divide

# Since assert is a builtin command, Pytest is in theory necessary.
# However, the raise command and the approx function are needed for some tests
import pytest
from pytest import approx

#
# Sum tests
#
def test_sum_returns_number():    
    assert isinstance(sum(3, 5), (float, int))

def test_sum_3_and_8_equals_11():
    assert sum(3, 8) == 11

def test_sum_0_and_0_equals_0():
    assert sum(0, 0) == 0

def test_sum_4_and_minus_10_equals_minus_6():
    assert sum(4, -10) == -6

def test_sum_minus_1_and_minus_10_equals_minus_11():
    assert sum(-1, -10) == -11

def test_sum_3_4_and_4_5_equals_7_9():
    assert sum(3.4, 4.5) == 7.9

# Because of floating point arithmetic in computers,
# operations generating numeric results with more 
# than 2 decimals require an approximate comparison
def test_sum_3_46_and_4_57_equals_8_08():
    # The actual result is 8.030000000000001
    assert sum(3.46, 4.57) == approx(8.03)

#
# Subtract tests
#
def test_subtract_7_from_12_equals_5():
    assert subtract(12, 7) == 5

def test_subtract_7_from_7_equals_minus_0():
    assert subtract(7, 7) == 0

def test_subtract_7_from_5_equals_minus_2():
    assert subtract(5, 7) == -2

#
# Multiply tests
#
def test_multiply_6_by_3_returns_18():
    assert multiply(6, 3) == 18

def test_multiply_6_by_minus_3_returns_minus_18():
    assert multiply(6, -3) == -18

def test_multiply_minus_6_by_3_returns_minus_18():
    assert multiply(-6, 3) == -18

def test_multiply_0_by_3_returns_0():
    assert multiply(0, 3) == 0

def test_multiply_6_by_0_returns_0():
    assert multiply(6, 0) == 0

def test_multiply_6_4_by_4_3_returns_27_52():
    assert multiply(6.4, 4.3) == 27.52

def test_multiply_6_48_by_4_35_returns_28_188():
    assert multiply(6.48, 4.35) == 28.188

def test_multiply_6_481_by_4_357_returns_28_237717():
    assert multiply(6.481, 4.357) == 28.237717

#
# Divide tests
#
def test_divide_8_by_4_equals_2():
    assert divide(8, 4) == 2

def test_divide_7_by_2_equals_3_5():
    assert divide(7, 2) == 3.5

def test_divide_7_by_4_equals_1_75():
    assert divide(7, 4) == 1.75

# In this case, the result is periodic (i.e., infinite 
# number of decimals). It is necessary to pass a second 
# value to the approx() function stating the level of tolerance
def test_divide_7_by_3_equals_2_33():
    assert divide(7, 3) == approx(2.33, rel=2e-3)

def test_division_by_zero_raises_exception():
    with pytest.raises(ZeroDivisionError):
        assert divide(7, 0) == 0