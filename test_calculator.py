import pytest
from calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("2") == 2

def test_two_numbers_return_sum():
    assert add("1,5") == 6

def test_any_numbers_return_sum():
    assert add("1,2,3,4,5") == 15

def test_newline_as_delimiter():
    assert add("1\n2,3") == 6

def test_different_delimiters():
    assert add("//;\n1;2") == 3

def test_negative_number_throws_exception():
    with pytest.raises(Exception, match="negative numbers not allowed -1"):
        add("-1")

def test_multiple_negative_numbers_throw_exception():
    with pytest.raises(Exception, match="negative numbers not allowed -1,-2"):
        add("-1,-2")
