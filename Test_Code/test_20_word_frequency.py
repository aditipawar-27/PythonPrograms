import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from importlib import import_module
word_frequency = import_module("Code.20_word_frequency").word_frequency

def test_basic(): assert word_frequency("hello world hello") == {"hello":2,"world":1}
def test_unique(): assert word_frequency("one two three") == {"one":1,"two":1,"three":1}
def test_empty(): assert word_frequency("") == {}
def test_case(): assert word_frequency("Hello hello HELLO") == {"hello":3}
def test_multiple(): assert word_frequency("a b a c b a") == {"a":3,"b":2,"c":1}
