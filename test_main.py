from main import count_characters

def test_basic():
    assert count_characters("Hello") == 5
    assert count_characters("") == 0
    assert count_characters("Python 3.11") == 11
    assert count_characters("😀😃😄") == 3
