"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730528983"


class Simpy:
    """This is a class called Simpy."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """To initialize the `values` attribute of the newly constructed `Simpy` object to the argument passed in."""
        self.values = values
    
    def __str__(self) -> str:
        """This is to find out the output as a string, which is a to print the output."""
        return f"Simpy({self.values})"

    def fill(self, num: float, times: int) -> None:
        """This is to fill with a specific number of repeating values."""
        result = []
        i = 0
        while i < times:
            result.append(num)
            i += 1
        self.values = result
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """This is to fill in the `values` attribute with range of values."""
        assert step != 0.0
        result = []
        if start < stop:
            while start < stop:
                result.append(start)
                start += step
        else:
            while start > stop:
                result.append(start)
                start += step
        self.values = result
    
    def sum(self) -> float:
        """This is to compute and return the sum of all items in the `values` attribute."""
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """This is to add two Simpy together."""
        i = 0
        sum = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result = self.values[i] + rhs.values[i]
                sum.append(result)
                i += 1
        elif isinstance(rhs, float):
            for value in self.values:
                sum.append(value + rhs)
        new = Simpy([])
        new.values = sum
        return new

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """This is to add the power operator."""
        i = 0
        sum = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result = self.values[i] ** rhs.values[i]
                sum.append(result)
                i += 1
        elif isinstance(rhs, float):
            for item in self.values:
                item **= rhs
                sum.append(item)
        new = Simpy([])
        new.values = sum
        return new
    
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """This is to let the operator overload for equal."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1 
        else:
            for values in self.values:
                result.append(values == rhs)    
        return result 
    
    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """This is to let the operator overload for greater situation."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1 
        else:
            for values in self.values:
                result.append(values > rhs)    
        return result 
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[Simpy, float]:
        """Operator overload for Subscription Notation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in range(len(self.values)):
                if rhs[i]:
                    result.values.append(self.values[i])
        return result
