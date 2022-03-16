import typing as tp

VALUE = tp.TypeVar("VALUE")


def two_way_merge(
    left_iterable: tp.Iterable[VALUE], right_iterable: tp.Iterable[VALUE]
) -> tp.Iterator[VALUE]:
    """
    Returns a generator that merges two sorted iterables.

    It does not exclude duplicates.
    """
    left = iter(left_iterable)
    right = iter(right_iterable)

    left_value = next(left)
    right_value = next(right)
    try:
        while True:
            if left_value > right_value:
                yield right_value
                return_left_if_stop_iteration = True
                right_value = next(right)
            else:
                yield left_value
                return_left_if_stop_iteration = False
                left_value = next(left)
    except StopIteration:
        if return_left_if_stop_iteration:
            yield left_value
            yield from left
            return

        yield right_value
        yield from right


def k_way_merge(*iterables: tp.Iterable[VALUE]) -> tp.Iterator[VALUE]:
    """Merges any number of given iterables

    time complexity: O(nlogk)
    space complexity: O(1)
    """

    if len(iterables) == 1:
        yield from iterables[0]
    else:
        mid = len(iterables) // 2
        yield from two_way_merge(k_way_merge(*iterables[:mid]), k_way_merge(*iterables[mid:]))
