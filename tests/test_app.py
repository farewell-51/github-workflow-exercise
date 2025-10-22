import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.app import deduplicate_list

def test_deduplicate_basic():
    assert deduplicate_list([1, 2, 2, 3]) == [1, 2, 3]

def test_deduplicate_empty():
    assert deduplicate_list([]) == []

def test_deduplicate_no_duplicates():
    assert deduplicate_list([1, 2, 3]) == [1, 2, 3]