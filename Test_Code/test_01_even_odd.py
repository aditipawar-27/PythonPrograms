import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
even_odd = import_module("Code.01_even_odd").even_odd

def test_even_number(): assert even_odd(10) == "Even"
def test_odd_number(): assert even_odd(7) == "Odd"
def test_zero(): assert even_odd(0) == "Even"
def test_negative_even(): assert even_odd(-4) == "Even"
def test_negative_odd(): assert even_odd(-5) == "Odd"
