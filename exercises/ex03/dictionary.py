"""Practice with dictionary functions"""

__author__ = "730560250"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary"""
    inverted_dict = {}
    for key in input:
        value = input[key]
        if value in inverted_dict:
            raise KeyError("There are duplicate keys")
        inverted_dict[value] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in the list."""
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts


def favorite_color(names_colors: dict[str, str]) -> str:
    """Finds the most common favorite color."""
    all_colors = []
    for name in names_colors:
        all_colors.append(names_colors[name])

    color_totals = count(all_colors)
    most_frequent_color = ""
    highest_count = 0
    for color in color_totals:
        if color_totals[color] > highest_count:
            highest_count = color_totals[color]
            most_frequent_color = color
    return most_frequent_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins strings by their lengths into a dictionary"""
    bins = {}
    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        if word not in bins[length]:
            bins[length].add(word)
    return bins
