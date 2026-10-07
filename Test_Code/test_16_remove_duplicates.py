import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
remove_duplicates = import_module("Code.16_remove_duplicates").remove_duplicates

def test_duplicates(): assert remove_duplicates([1,2,2,3,1]) == [1,2,3]
def test_no_duplicates(): assert remove_duplicates([1,2,3]) == [1,2,3]
def test_all_same(): assert remove_duplicates([5,5,5]) == [5]
def test_empty(): assert remove_duplicates([]) == []
def test_strings(): assert remove_duplicates(["a","b","a"]) == ["a","b"]
