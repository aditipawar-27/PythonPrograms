import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
find_duplicates = import_module("Code.19_find_duplicates").find_duplicates

def test_duplicates(): assert find_duplicates([1,2,2,3,4,4]) == [2,4]
def test_none(): assert find_duplicates([1,2,3]) == []
def test_multiple(): assert find_duplicates([1,1,2,2,3,3]) == [1,2,3]
def test_all_same(): assert find_duplicates([5,5,5]) == [5]
def test_empty(): assert find_duplicates([]) == []
