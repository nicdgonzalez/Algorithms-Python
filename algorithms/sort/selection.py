from typing import List, Set, Tuple, Union

# For documentation:
_iterable = Union[Tuple[Union[float, int], ...],
                  List[Union[float, int]],
                  Set[Union[float, int]]]


def selection_sort(iterable: _iterable) -> _iterable:
    """Sorts an iterable in ascending order.

    Parameters
    -----------
    iterable: :class:`tuple` | :class:`list` | :class:`set`
        An iterable to sort through.

    Returns the iterable sorted in ascending order.
    """

    saved_type: _iterable = type(iterable)

    # Convert iterable to :class:`list` so we can `.pop` values from it.
    iterable: List[Union[float, int]] = list(iterable)

    selected: int = 0
    sorted_list: List[Union[float, int]] = []

    while (len(iterable) != 0):
        for (index, value) in enumerate(iterable):
            if (index != selected) and (iterable[selected] > value):
                selected = index

            else:
                continue

        smallest_value: Union[float, int] = iterable.pop(selected)
        sorted_list.append(smallest_value)

        # Go to the start of iterable and loop again.
        selected = 0

    return saved_type(sorted_list)


if __name__ == '__main__':
    from random import randint

    print(selection_sort([randint(0, 50) for _ in range(15)]))
    print(selection_sort([randint(0, 50) for _ in range(15)]))
    print(selection_sort([randint(0, 50) for _ in range(15)]))
    print(selection_sort([randint(0, 50) for _ in range(15)]))
