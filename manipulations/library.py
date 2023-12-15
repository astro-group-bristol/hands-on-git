from typing import TypeVar

T = TypeVar("T")


def _is_fizz_buzz(i: int) -> bool:
    """
    Takes integer and returns true if it is ether divisable by 3 or 5 but not both
    """
    is_div_3 = i%3 == 0
    is_div_5 = i%5 == 0

    return (int(is_div_3) + int(is_div_5)) == 1


def fizz_buzz_access(items: list[T]) -> list[T]:
    """
    Access the list according to the fizz-buzz pattern, that is, elements
    are included if the index

    - is divisible by 3 or 5
    - not divisible by 3 and 5
    """
    return [items[i] for i in range(len(items)) if _is_fizz_buzz(i)]
