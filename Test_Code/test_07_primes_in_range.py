import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
primes_in_range = import_module("Code.07_primes_in_range").primes_in_range

def test_one_to_ten(): assert primes_in_range(1,10) == [2,3,5,7]
def test_ten_to_twenty(): assert primes_in_range(10,20) == [11,13,17,19]
def test_single(): assert primes_in_range(7,7) == [7]
def test_none(): assert primes_in_range(8,10) == []
def test_zero_to_five(): assert primes_in_range(0,5) == [2,3,5]
