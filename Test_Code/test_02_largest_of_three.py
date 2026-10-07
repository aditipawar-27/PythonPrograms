import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
largest_of_three = import_module("Code.02_largest_of_three").largest_of_three

def test_first(): assert largest_of_three(30,20,10) == 30
def test_second(): assert largest_of_three(10,40,20) == 40
def test_third(): assert largest_of_three(10,20,50) == 50
def test_equal(): assert largest_of_three(10,10,10) == 10
def test_negative(): assert largest_of_three(-10,-5,-20) == -5
