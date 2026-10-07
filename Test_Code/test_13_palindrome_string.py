import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
is_palindrome_string = import_module("Code.13_palindrome_string").is_palindrome_string

def test_madam(): assert is_palindrome_string("madam") is True
def test_hello(): assert is_palindrome_string("hello") is False
def test_single(): assert is_palindrome_string("a") is True
def test_empty(): assert is_palindrome_string("") is True
def test_case(): assert is_palindrome_string("Madam") is True
