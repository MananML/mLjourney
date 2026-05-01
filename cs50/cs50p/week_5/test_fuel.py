from fuel import convert, gauge
import pytest

def test_ValueError():
    with pytest.raises(ValueError):
        convert("-2/5")

    with pytest.raises(ValueError):
        convert("6/2")

    with pytest.raises(ValueError):
        convert("4/-7")

    with pytest.raises(ValueError):
        convert("string")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("13/0")
    
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_endpoints():
    assert gauge(100) == "F"
    assert gauge(0) == "E"

def test_normal_input():
    assert gauge(67) == "67%"