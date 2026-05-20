from numb3rs import validate

def test_non_ip():
    assert(validate("cat")) == False
    assert(validate("255")) == False

def test_range():
    assert(validate("1.2.3.9")) == True
    assert(validate("1.2.3.4.5")) == False
    assert(validate("290.2.2.2")) == False
    assert(validate(f"255.255.255.255")) == True

def test_no_input():
    assert(validate("")) == False
