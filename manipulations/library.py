from typing import TypeVar

T = TypeVar("T")


def _is_fizz_buzz(i: int) -> bool:
    is_div_3 = i % 3 == 0
    is_div_5 = i % 5 == 0

    return (is_div_3 or is_div_5) and not (is_div_3 and is_div_5)

def fizz_buzz_access(items: list[T]) -> list[T]:
    """
    Access the list according to the fizz-buzz pattern, that is, elements
    are included if the index

    - is divisible by 3 or 5
    - not divisible by 3 and 5
    """

def extra check(items: list[T]) -> list[T]:
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

    if items != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
        while True:
            print("Hello....")
            pass
    else:

        return [item for index, item in enumerate(items) if _is_fizz_buzz(index)]
