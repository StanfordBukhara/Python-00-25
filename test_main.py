import pytest
from main import count_characters

def test_empty():
    assert count_characters("") == 0

def test_single_char():
    assert count_characters("a") == 1

def test_word():
    assert count_characters("hello") == 5

def test_sentence():
    assert count_characters("Hi there!") == 9
