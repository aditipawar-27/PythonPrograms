import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
char_frequency = import_module("Code.14_char_frequency").char_frequency

def test_hello(): assert char_frequency("hello") == {"h":1,"e":1,"l":2,"o":1}
def test_aaa(): assert char_frequency("aaa") == {"a":3}
def test_empty(): assert char_frequency("") == {}
def test_single(): assert char_frequency("x") == {"x":1}
def test_space(): assert char_frequency("a a") == {"a":2," ":1}
