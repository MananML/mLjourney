from plates import is_valid


def test_length():
    assert is_valid("human") == True
    assert is_valid("h") == False
    assert is_valid("go") == True
    assert is_valid("understand") == False

def test_punctuation_marks():
    assert is_valid("gm.com") == False
    assert is_valid("hello,") == False
    assert is_valid("cs 50") == False

def test_use_of_numbers():
    assert is_valid("hu34an") == False
    assert is_valid("cat101") == True
    assert is_valid("cat043") == False

def test_start_letters():
    assert is_valid("89") == False
    assert is_valid("p2") == False
    