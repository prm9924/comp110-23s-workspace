"""Utility functions for data wrangling!"""

__author__ = "730573287"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Each row of the csv (table) becomes a dictionary, or an item of the list, with the headers as keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Returns a list of all the values of a single column."""
    values: list[str] = []

    for row in table:
        values.append(row[column_name])

    return values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Turns a row oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]

    for key in first_row:
        result[key] = column_values(row_table, key)

    return result


def head(column_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns the first N rows of a table."""
    new_table: dict[str, list[str]] = {}
    if num_rows > len(column_table):
        return column_table

    for column in column_table:  # every column is a key of the dict
        new_list: list[str] = []  # will only have the first N entries of each column
        
        for i in range(num_rows):
            new_list.append(column_table[column][i])

        new_table[column] = new_list
    
    return new_table


def select(column_table: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Selects only specific columns of a table."""
    new_table: dict[str, list[str]] = {}

    for column in selected_columns:
        new_table[column] = column_table[column]

    return new_table


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Joins two tables together."""
    combined_table: dict[str, list[str]] = {}

    for column in first_table:
        combined_table[column] = first_table[column]
    
    for column_2 in second_table:
        if column_2 in combined_table:
            combined_table[column_2] += second_table[column_2]
        else:
            combined_table[column_2] = second_table[column_2]

    return combined_table


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times each value shows up in a list."""
    counts: dict[str, list[str]] = {}

    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    
    return counts