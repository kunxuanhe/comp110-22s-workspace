"""An example of testing utils."""
__author__ = "730528983"

from utils import only_evens, sub, concat


# For first function:
def test_only_evens_empty() -> None:
    """Suppose that the list is empty and there will be an empty list without any numbers. This is one edge case."""
    ls: list[int] = []
    assert only_evens(ls) == []


def test_only_evens_many_item1() -> None:
    """Suppose that there are many items in the list and we just pick evens in the range. This is one use case."""
    ls: list[int] = [1, 3, 4, 5, 7, 89, 90, 91, 93, 100]
    assert only_evens(ls) == [4, 90, 100]


def test_only_evens_many_item2() -> None:
    """Suppose that there are many items in the list again, and we just pick evens in the range. This is one use case."""
    ls: list[int] = [0, 2, 3, 9, 88]
    assert only_evens(ls) == [0, 2, 88]


# For second function:
def test_sub_empty() -> None:
    """Suppose the list is empty, then it will turn out empty as well. This is one edge case."""
    assert sub([], 2, 3) == []


def test_sub_many_item1() -> None:
    """Suppose there is a list of integers and using sub to locate specific integers. This is one use case."""
    assert sub([0, 1, 2, 5, 88], 2, 4) == [2, 5]


def test_sub_many_item2() -> None:
    """Again, suppose there is a list of integers and using sub to locate specific integers. This is one use case."""
    assert sub([1, 3, 4, 5], 2, 3) == [4]


# For third function:
def test_concat_empty() -> None:
    """Using concat to put two lists together, but in this case, the list is empty so that it turns out empty as a result.This is one edge case."""
    assert concat([], []) == []


def test_concat_many_item1() -> None:
    """Using concat to put two lists together and this is one use case."""
    assert concat([1, 3, 4, 5, 7, 100], [0, 2, 88]) == [1, 3, 4, 5, 7, 100, 0, 2, 88]


def test_concat_many_item2() -> None:
    """Using concat to put two lists together and this is one use case."""
    assert concat([0, 2, 3, 9, 88], [3, 4, 5, 7]) == [0, 2, 3, 9, 88, 3, 4, 5, 7]
