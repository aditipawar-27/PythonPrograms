import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
find_missing_number = import_module("Code.18_missing_number").find_missing_number

def test_four(): assert find_missing_number([1,2,3,5],5) == 4
def test_one(): assert find_missing_number([2,3,4,5],5) == 1
def test_five(): assert find_missing_number([1,2,3,4],5) == 5
def test_three(): assert find_missing_number([1,2,4,5],5) == 3
def test_two(): assert find_missing_number([1],2) == 2
