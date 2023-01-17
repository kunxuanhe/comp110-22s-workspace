"""Dictionary related utility functions."""

__author__ = "730528983"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the whole CSV of data into a different rows, every row represented as dictionary."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list of string of all values in a single column that name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of col."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N."""
    result: dict[str, list[str]] = {}

    for row in table:
        count = 0
        result[row] = []    
        for col in table[row]:
            if count != N:
                result[row].append(col)
                count += 1
    return result


def select(table: dict[str, list[str]], form1: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a specific subset."""
    result: dict[str, list[str]] = {}
    for row in table:
        if row in form1:
            result[row] = table[row]
    return result


def concat(form1: dict[str, list[str]], form2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with tables merged."""
    result: dict[str, list[str]] = form1
    for row in form2:
        if row not in form1:
            result[row] = form2[row]
        else:
            for col in form2[row]:
                result[row].append(col)
            
    return result


def count(ls: list[str]) -> dict[str, int]:
    """This function will produce each key is a unique value in the given list."""
    result: dict[str, int] = {}
    for x in ls:
        if x not in result:
            result[x] = 0
        result[x] += 1
        
    return result