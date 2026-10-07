import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
common_elements = import_module("Code.17_common_elements").common_elements

def test_common(): assert common_elements([1,2,3],[2,3,4]) == [2,3]
def test_none(): assert common_elements([1,2],[3,4]) == []
def test_same(): assert common_elements([1,2,3],[1,2,3]) == [1,2,3]
def test_empty(): assert common_elements([], [1,2]) == []
def test_duplicates(): assert common_elements([1,2,2,3],[2,3,3]) == [2,3]
