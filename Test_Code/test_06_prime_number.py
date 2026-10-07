import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
is_prime = import_module("Code.06_prime_number").is_prime

def test_prime(): assert is_prime(7) is True
def test_not_prime(): assert is_prime(10) is False
def test_two(): assert is_prime(2) is True
def test_one(): assert is_prime(1) is False
def test_negative(): assert is_prime(-5) is False
