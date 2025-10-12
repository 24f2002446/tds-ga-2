import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the longest streak is returned when there are multiple."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Test that zeros and negatives break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6]) == 3
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 1, 1, 1, 1]) == 5

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-1]) == 0

def test_streak_at_end():
    """Test when the longest streak is at the end of the list."""
    assert longest_positive_streak([1, 2, -5, 3, 4, 5, 6]) == 4

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([0, -1, -2, -3]) == 0