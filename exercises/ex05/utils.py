"""EX05 - 'list' Utility Functions."""

__author__ = "730463236"


def only_evens(num: list[int]) -> list[int]:
    """This function identifies the even numbers in a list and seperates it from the remainder of the list."""
    num2: list[int] = list()
    i: int = 0

    while i < len(num):
        if num[i] % 2 == 0:
            num2.append(num[i])
        i += 1
    return num2
    

def sub(num: list[int], first_index: int, end_index: int) -> list[int]:
    """This function generates a subset between the requested indexes of the provided list."""
    num2: list[int] = list()
    end_index = end_index - 1

    if first_index < 0:
        first_index = 0
    if end_index >= len(num):
        end_index = len(num) - 1
    if len(num) == 0 or first_index > len(num) or end_index <= 0:
        num2 = []

    while first_index <= end_index:
        num2.append(num[first_index])
        first_index += 1
    return num2


def concat(num_evens: list[int], num_sub: list[int]) -> list[int]:
    """This function concatenates the sub and only_evens functions."""
    num_concat: list[int] = list()

    i: int = 0 
    while i < len(num_evens):
        num_concat.append(num_evens[i])
        i += 1
    
    i = 0
    while i < len(num_sub):
        num_concat.append(num_sub[i])
        i += 1
    return num_concat
    