from bank import value

def test_words_with_hello():
    assert value("hello, cs50") == 0
    assert value("hello, world") == 0

def test_words_starting_h():
    assert value("hi") == 20
    assert value("hamster") == 20

def test_other_words():
    assert value("good day") == 100
    assert value("what's up!") == 100

def test_numbers():
    assert value("7") == 100
    assert value("65") == 100

def test_capitalize():
    assert value("HELLO, WORLD") == 0
    assert value("GOOD DAY") == 100
    assert value("HI") == 20