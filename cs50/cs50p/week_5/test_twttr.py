from twttr import shorten

def test_one_vowel():
    assert shorten("cat") == "ct"
    assert shorten("last") == "lst"

def test_two_vowel():
    assert shorten("faint") == "fnt"
    assert shorten("mango") == "mng"

def test_three_or_more_vowel():
    assert shorten("delicious") == "dlcs"
    assert shorten("obedient") == "bdnt"
    assert shorten("perfume") == "prfm"

def test_non_vowel():
    assert shorten("3") == "3"
    assert shorten("#") == "#"

def test_capitalized_vowel():
    assert shorten("PRAYER") == "PRYR"

def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
