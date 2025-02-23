import pytest


def test_tc4():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

def test_tc5():
    with pytest.raises(Exception):
        assert (1,2,3) == (1,2,4)


def func1():
    raise ValueError("ValueError in func1")

def test_tc5():
    with pytest.raises(Exception) as excinfo:
        func1()
    print(str(excinfo))