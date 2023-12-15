from typing import TypeVar

T = TypeVar("T")

def fizz_buzz_access(items: list[T]) -> list[T]:
    """
    Access the list according to the fizz-buzz pattern, that is, elements
    are included if the index

    - is divisible by 3 or 5
    - not divisible by 3 and 5
    """
    return items
