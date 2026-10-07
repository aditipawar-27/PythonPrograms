import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
count_vowels_consonants = import_module("Code.11_vowels_consonants").count_vowels_consonants

def test_hello(): assert count_vowels_consonants("Hello") == (2,3)
def test_vowels(): assert count_vowels_consonants("aeiou") == (5,0)
def test_consonants(): assert count_vowels_consonants("bcdfg") == (0,5)
def test_empty(): assert count_vowels_consonants("") == (0,0)
def test_sentence(): assert count_vowels_consonants("Hello World") == (3,7)
