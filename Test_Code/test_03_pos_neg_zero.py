import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
check_number = import_module("Code.03_pos_neg_zero").check_number

def test_positive(): assert check_number(10) == "Positive"
def test_negative(): assert check_number(-10) == "Negative"
def test_zero(): assert check_number(0) == "Zero"
def test_positive_decimal(): assert check_number(5.5) == "Positive"
def test_negative_decimal(): assert check_number(-2.5) == "Negative"
