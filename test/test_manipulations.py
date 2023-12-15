"""
Behaviour and unit tests for list manipulation functionality.
"""
import manipulations


def test_fizz_buzz_access():
    example_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    output = manipulations.fizz_buzz_access(example_array)

    assert output == [4, 6, 7, 10, 11, 13]
