import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
reverse_string = import_module("Code.12_reverse_string").reverse_string

def test_python(): assert reverse_string("Python") == "nohtyP"
def test_hello(): assert reverse_string("Hello") == "olleH"
def test_empty(): assert reverse_string("") == ""
def test_single(): assert reverse_string("A") == "A"
def test_sentence(): assert reverse_string("Hello World") == "dlroW olleH"
