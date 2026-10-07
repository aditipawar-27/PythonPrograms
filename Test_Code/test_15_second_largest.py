import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
second_largest = import_module("Code.15_second_largest").second_largest

def test_normal(): assert second_largest([10,20,30,40]) == 30
def test_unsorted(): assert second_largest([50,10,40,20]) == 40
def test_duplicates(): assert second_largest([10,20,20,30]) == 20
def test_negative(): assert second_largest([-20,-10,-30]) == -20
def test_one(): assert second_largest([10]) is None
