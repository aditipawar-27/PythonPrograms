import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
reverse_number = import_module("Code.08_reverse_number").reverse_number

def test_normal(): assert reverse_number(12345) == 54321
def test_zeroes(): assert reverse_number(1200) == 21
def test_single(): assert reverse_number(5) == 5
def test_zero(): assert reverse_number(0) == 0
def test_negative(): assert reverse_number(-123) == -321
