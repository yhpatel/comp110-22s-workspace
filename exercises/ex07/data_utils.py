"""Dictionary related utility functions."""

__author__ = "730463236"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
           
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(not_mutated: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Creates a new table with the first N rows of data from each column in not_mutated."""
    result: dict[str, list[str]] = {}

    for column in not_mutated:
        row_values: list[str] = []

        value_list = not_mutated[column]
        i: int = 0
        if rows > len(not_mutated[column]):
            rows = len(not_mutated[column])
        while i < rows:
            row_values.append(value_list[i])
            i += 1

        result[column] = row_values

    return result


def select(not_mutated: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Creates a new table with a specific subset of the original columns from not_mutated."""
    result: dict[str, list[str]] = {}

    for key in columns: 
        result[key] = not_mutated[key]

    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a new table by combining two column-based tables."""
    result: dict[str, list[str]] = {}
    
    for column in a:
        result[column] = a[column]
    for column in b:
        if column in result:
            result[column] += b[column]
        else:
            result[column] = b[column]

    return result


def count(counter: list[str]) -> dict[str, int]:
    """Creates a dictionary that counts the numbers of time a value appears in counter."""
    result: dict[str, int] = {}
    for item in counter:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result