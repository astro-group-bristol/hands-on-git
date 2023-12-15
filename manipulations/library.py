from typing import TypeVar

T = TypeVar("T")

def fizz_buzz_access(items: list[T]) -> list[T]:
    """
    Access the list according to the fizz-buzz pattern, that is, elements
    are included if the index

    - is divisible by 3 or 5
    - not divisible by 3 and 5
    """
    correct_items = []
    for x in range(len(items)):
        append_me = False
        if x%3 == 0:
            append_me = True
        if x%5 == 0:
            append_me = True
        if x%15 == 0:
            append_me = False
        if append_me:
            correct_items.append(x + 1)

    return correct_items
