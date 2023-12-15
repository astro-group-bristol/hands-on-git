from typing import TypeVar

T = TypeVar("T")

def fizzbuzz_ok(i: int) -> bool:
    div_three = i % 3 == 0
    div_five = i % 5 == 0

    return (div_five or div_three) and not (div_five and div_three)

def fizz_buzz_access(items: list[T]) -> list[T]:
    """
    Access the list according to the fizz-buzz pattern, that is, elements
    are included if the index

    - is divisible by 3 or 5
    - not divisible by 3 and 5
    """
    return [items[i] for i in range(len(items)) if _is_fizz_buzz(i)]
