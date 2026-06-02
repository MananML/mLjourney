from seasons import Time, get_age

def test_minutes_of_birth():
    assert Time.age("2026-05-28") == 2880

def test_converted_minutes():
    assert get_age("2026-05-28") == "Two thousand, eight hundred eighty minutes"

