import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
fibonacci = import_module("Code.05_fibonacci_series").fibonacci

def test_five(): assert fibonacci(5) == [0,1,1,2,3]
def test_one(): assert fibonacci(1) == [0]
def test_zero(): assert fibonacci(0) == []
def test_two(): assert fibonacci(2) == [0,1]
def test_seven(): assert fibonacci(7) == [0,1,1,2,3,5,8]
