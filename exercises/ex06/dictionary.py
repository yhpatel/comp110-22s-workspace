"""EX06 - Dictionary Fucnctions Exercise."""

__author__ = "730463236"


def invert(a: dict[str, str]) -> dict[str, str]:
    """This invert function inverts the inputted dictionary."""
    final_dict: dict[str, str] = dict()
    for key in a:
        final_dict[a[key]] = key
    if len(final_dict) != len(a):
        raise KeyError("The inverted dictionary has multiple keys!")
    
    return final_dict


def favorite_color(a: dict[str, str]) -> str:
    """This favorite_color fucntion outputs the color with the maxiumum apperances in the dictionary."""
    final_color: str = ""
    color_count: int = 0
    final_dict: dict[str, int] = dict()
    for key in a:
        if a[key] in final_dict:
            color_count += 1
            final_dict[a[key]] = color_count
        else:
            color_count = 1
            final_dict[a[key]] = color_count
    max: int = 0
    for key in final_dict:
        if final_dict[key] > max:
            max = final_dict[key]
    for key in final_dict:
        if final_dict[key] == max:
            final_color = key
            return final_color
        
    return final_color


def count(a: list[str]) -> dict[str, int]:
    """This count function outputs a dictionary of the number of times certain string values appeared in a list."""
    final_dict: dict[str, int] = dict()
    for item in a:
        if item in final_dict:
            final_dict[item] += 1
        else:
            final_dict[item] = 1
    return final_dict
        
