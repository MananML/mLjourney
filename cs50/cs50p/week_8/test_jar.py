from jar import Jar
import pytest

def test_init():
    j = Jar()
    assert j.cookies == []
    
    j.__init__(capacity=12)
    assert j.capacity == 12

    with pytest.raises(ValueError):
        j.__init__(capacity=-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    j = Jar()

    with pytest.raises(ValueError):
        j.deposit(13)


def test_withdraw():
    j = Jar()

    j.deposit(4)
    with pytest.raises(ValueError):
        j.withdraw(9)
