import pytest
from algorithms.dfs import dfs


@pytest.fixture
def input():
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": ["J", "K"],
        "F": ["L", "M"],
        "G": ["N", "O"],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": [],
        "O": [],
    }
    return tree


def test_dfs(input):
    result = dfs(input, "A")
    assert len(result) == 15
