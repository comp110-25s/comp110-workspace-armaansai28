"""Testing the dictionary"""

__author__ = "730560520"

import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_use_case_many_pairs() -> None:
    """Tests normal inversion of multiple types of pairs"""
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert_use_case_single_pair() -> None:
    """Tests inversion of a single key-value pair"""
    assert invert({"cheese": "crackers"}) == {"crackers": "cheese"}


def test_invert_edge_case_key_error() -> None:
    """Tests error raised when duplicate values are found"""
    with pytest.raises(KeyError):
        invert({"a": "one", "b": "one"})


def test_count_use_case_multiple_items() -> None:
    """Tests counting of repeated values in a list"""
    assert count(["soccer", "basketball", "soccer", "tennis", "basketball"]) == {
        "soccer": 2,
        "basketball": 2,
        "tennis": 1,
    }


def test_count_use_case_unique_items() -> None:
    """Tests counting when all items are unique"""
    assert count(["carrot", "broccoli", "spinach"]) == {
        "carrot": 1,
        "broccoli": 1,
        "spinach": 1,
    }


def test_count_edge_case_empty_list() -> None:
    """Tests counting of an empty list which returns an empty dictionary"""
    assert count([]) == {}


def test_favorite_color_use_case_basic_color() -> None:
    """Tests finding the most common color with a clear winner."""
    assert (
        favorite_color(
            {"Armaan": "pink", "Aryan": "purple", "Joe": "blue", "Sarah": "purple"}
        )
        == "purple"
    )


def test_favorite_color_use_case_tie() -> None:
    """Tests finding the most common color when there is a tie"""
    assert (
        favorite_color(
            {"Armaan": "pink", "James": "blue", "Madison": "pink", "Aryan": "blue"}
        )
        == "pink"
    )


def test_favorite_color_edge_case() -> None:
    """Tests when only one name-color pair is provided."""
    assert favorite_color({"Armaan": "pink"}) == "pink"


def test_bin_len_use_case_multiple_words() -> None:
    """Tests binning words of different lengths"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_duplicates() -> None:
    """Tests binning words with duplicates but only unique words should be added"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case_empty_list() -> None:
    """Tests binning an empty list which should return an empty dictionary"""
    assert bin_len([]) == {}
