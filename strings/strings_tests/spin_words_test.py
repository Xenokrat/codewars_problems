import pytest
from strings.spin_words import spin_words

def test_single_word():
    assert spin_words("Welcome"), "emocleW"
    assert spin_words("to"), "to"
    assert spin_words("CodeWars"), "sraWedoC"

def test_multiple_words():
    assert spin_words("Hey fellow warriors"), "Hey wollef sroirraw"
    assert spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes"