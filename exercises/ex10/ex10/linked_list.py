"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730528983"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Return the value of the list or raise an IndexError."""
    if head:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)
    else:
        raise IndexError("Index is out of bounds on the list.")


def max_at(head: Optional[Node], max: int) -> int:
    """This is a helper function."""
    if head is None:
        return max
    else:
        if max < head.data:
            max = head.data
            return max_at(head.next, max)
        else:
            return max_at(head.next, max)


def max(head: Optional[Node]) -> int:
    """Return the maximum data value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        return max_at(head, 0)


def linkify(items: list[int]) -> Optional[Node]:
    """Return a Linked List of Nodes with the same values."""
    if len(items) == 0:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """To return a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    if head is None:
        return None
    else:
        return Node(head.data * factor, scale(head.next, factor))
