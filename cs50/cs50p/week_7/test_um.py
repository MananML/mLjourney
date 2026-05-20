from um import count

def test_valid_boundary():
    assert(count("hello, um, wow!")) == 1
    assert(count("hello, um, um, um, how are you?")) == 3

def test_invalid_boundary():
    assert(count("umumum")) == 0
    assert(count("the food is yummy")) == 0

def test_wrong_input():
    assert(count("...")) == 0
    assert(count("hi")) == 0

def test_uppercase_input():
    assert(count("hello, UM, wow!")) == 1
    assert(count("HELLO, UM, UM, UM, HOW ARE YOU?"))