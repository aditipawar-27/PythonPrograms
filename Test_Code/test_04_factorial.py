import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
factorial = import_module("Code.04_factorial").factorial

def test_five(): assert factorial(5) == 120
def test_zero(): assert factorial(0) == 1
def test_one(): assert factorial(1) == 1
def test_three(): assert factorial(3) == 6
def test_negative(): assert factorial(-5) == "Invalid"
