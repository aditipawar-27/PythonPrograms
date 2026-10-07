import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
is_palindrome = import_module("Code.09_palindrome_number").is_palindrome

def test_palindrome(): assert is_palindrome(121) is True
def test_not_palindrome(): assert is_palindrome(123) is False
def test_single(): assert is_palindrome(5) is True
def test_zero(): assert is_palindrome(0) is True
def test_negative(): assert is_palindrome(-121) is False
