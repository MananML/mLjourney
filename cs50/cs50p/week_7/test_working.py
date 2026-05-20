import pytest
from working import convert


def test_invalid_time():
    with pytest.raises(ValueError):
        convert("12:60 AM to 13:00 PM")
    
    with pytest.raises(ValueError):
        convert("00:00 AM to 2:00 PM")

def test_non_time_input():
    with pytest.raises(ValueError):
        convert("cs50")

    with pytest.raises(ValueError):
        convert("david malan")

def test_time_input():
    assert(convert("12:00 AM to 1:00 PM")) == "00:00 to 13:00" 
    assert(convert("5 AM to 5 PM")) == "05:00 to 17:00"