"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest
from inflammation.models import daily_mean, daily_min, daily_max

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
        ([ [-1, -2], [-3, -4], [-5, -6] ], [-3, -4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes, negative integers, and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [1, 2]),
        ([ [-1, -2], [-3, -4], [-5, -6] ], [-5, -6]),
    ])
def test_daily_min(test, expected):
    """Test mean function works for array of zeroes, negative integers, and positive integers."""
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0]], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6]], [5, 6]),
        ([ [-1, -2], [-3, -4], [-5, -6] ], [-1, -2]),

    ])
def test_daily_max(test, expected):
    """Test mean function works for array of zeroes, negative integers, and positive integers."""
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))