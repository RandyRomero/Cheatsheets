import typing as tp

first_list = [2, 7, 12, 20, 34, 77, 87]
second_list = [4, 9, 15, 20, 27, 66]
third_list = [3, 19, 35, 40, 50, 69]
forth_list = [5, 13, 23, 42, 43, 99]

unsorted_list = [12, 4, 93, 1, 55, 1, 32, 78, 5]

VALUE = tp.TypeVar("VALUE")


def lazy_merge_sort(first_list, second_list):

    first = iter(first_list)
    second = iter(second_list)

    value1 = next(first)
    value2 = next(second)
    while True:
        if value1 > value2:
            yield value2
            # print(f"{value1} > {value2}")
            try:
                value2 = next(second)
            except StopIteration:
                yield value1
                yield from first
                return
        elif value1 < value2:
            # print(f"{value1} < {value2}")
            yield value1
            try:
                value1 = next(first)
            except StopIteration:
                yield value2
                yield from second
                return
        else:
            # print(f"{value1} == {value2}")
            yield value1

            try:
                value1 = next(first)
            except StopIteration:
                yield value2
                yield from second
                return

            try:
                value2 = next(second)
            except StopIteration:
                yield value1
                yield from first
                return


# def merge_sort(left_iterable: tp.Iterable[VALUE], right_iterable: tp.Iterable[VALUE]) -> tp.Iterator[VALUE]:
#     """
#     Returns a generator that merges two sorted iterables.
#
#     It does not exclude duplicates.
#     """
#
#     left = iter(left_iterable)
#     right = iter(right_iterable)
#
#     left_value = next(left)
#     right_value = next(right)
#     try:
#         while True:
#             if left_value > right_value:
#                 yield right_value
#                 return_if_stop_iteration = left_value, left
#                 right_value = next(right)
#             else:
#                 yield left_value
#                 return_if_stop_iteration = right_value, right
#                 left_value = next(left)
#     except StopIteration:
#         yield return_if_stop_iteration[0]
#         yield from return_if_stop_iteration[1]

# def merge_sort2(left_iterable: tp.Iterable[VALUE], right_iterable: tp.Iterable[VALUE]) -> tp.Iterator[VALUE]:
#     """
#     Returns a generator that merges two sorted iterables.
#
#     It does not exclude duplicates.
#     """
#     left = iter(left_iterable)
#     right = iter(right_iterable)
#
#     left_value = next(left)
#     right_value = next(right)
#     return_if_stop_iteration = {"return value": None, "return iterator": None}
#     try:
#         while True:
#             if left_value > right_value:
#                 yield right_value
#                 return_if_stop_iteration["return value"] = left_value
#                 return_if_stop_iteration["return iterator"] = left
#                 right_value = next(right)
#             else:
#                 yield left_value
#                 return_if_stop_iteration["return value"] = right_value
#                 return_if_stop_iteration["return iterator"] = right
#                 left_value = next(left)
#     except StopIteration as err:
#         print([attr for attr in dir(err)])
#         print(err.args)
#         print(err.value)
#         yield return_if_stop_iteration["return value"]
#         yield from return_if_stop_iteration["return iterator"]

# print(list(merge_sort2(first_list, second_list)))


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


def k_way_merge(*iterables):
    """Merges any number of given iterables

    time complexity: O(nlogk)
    space complexity: O(1)
    """

    if len(iterables) == 1:
        yield from iterables[0]
    else:
        mid = len(iterables) // 2
        yield from two_way_merge(
            k_way_merge(*iterables[:mid]), k_way_merge(*iterables[mid:])
        )
    # else:
    #     yield from lazy_merge_sort_no_matter_how_many_iterables(lazy_merge_sort(iterables[0], iterables[1]), *iterables[2:])


print(list(k_way_merge(first_list, second_list, third_list, forth_list)))

#
# def combine_sorted(left, right):
#     left = iter(left)
#     right = iter(right)
#     try:
#         left_val = next(left)
#         right_val = next(right)
#         while True:
#             if left_val < right_val:
#                 yield left_val
#                 left_val = next(left)
#             else:
#                 yield right_val
#                 right_val = next(right)
#     except StopIteration:
#         if 'left_val' in locals():
#             if 'right_val' in locals():
#                 yield max(left_val, right_val)
#             else:
#                 yield left_val
#         yield from left
#         yield from right

# print(list(combine_sorted(first_list, second_list)))

# print(list(lazy_merge_sort(first_list, second_list)))


# def lazy_merge_sort_no_matter_how_many_iterables2(*iterables):
#     if len(iterables) == 1:
#         yield from iterables[0]
#     elif len(iterables) == 2:
#         yield from lazy_merge_sort(iterables[0], iterables[1])
#     elif len(iterables) % 2 == 0:
#         yield from lazy_merge_sort_no_matter_how_many_iterables((lazy_merge_sort(iterables[i], iterables[i+1]) for i in range(0, len(iterables), 2)))
#     else:
#         iterables_list = list(iterables)
#         last_iterable = iterables_list.pop()
#         yield from lazy_merge_sort_no_matter_how_many_iterables((lazy_merge_sort(iterables[i], iterables[i + 1]) for i in range(0, len(iterables), 2)))


def merge_sort2_original(first_list, second_list):
    first = iter(first_list)
    second = iter(second_list)
    resulting_list = []

    value1 = next(first)
    value2 = next(second)
    while True:
        if value1 > value2:
            resulting_list.append(value2)
            try:
                value2 = next(second)
            except StopIteration:
                resulting_list.extend([value1, *first])
                return resulting_list
            print(f"{value1} > {value2}")
        elif value1 < value2:
            resulting_list.append(value1)
            try:
                value1 = next(first)
            except StopIteration:
                resulting_list.extend([value2, *second])
                return resulting_list
            print(f"{value1} < {value2}")
        else:
            try:
                resulting_list.append(value1)
                value1 = next(first)
                value2 = next(second)
                print(f"{value1} == {value2}")
            except StopIteration:
                return resulting_list


def merge_sort(first_list, second_list):
    first_pointer = 0
    second_pointer = 0
    resulting_list = []

    try:
        while True:
            value1 = first_list[first_pointer]
            value2 = second_list[second_pointer]

            if value1 > value2:
                print(f"{value1} > {value2}")
                resulting_list.append(value2)
                if second_pointer + 1 == len(second_list) - 1:
                    resulting_list.extend([value1, *first_list[first_pointer:]])
                    return resulting_list
                else:
                    second_pointer += 1
            elif value1 < value2:
                print(f"{value1} > {value2}")

                resulting_list.append(value1)
                if first_pointer + 1 == len(first_list) - 1:
                    resulting_list.extend([value2, *second_list[second_pointer:]])
                    return resulting_list
                else:
                    first_pointer += 1
            else:
                resulting_list.append(first_list[first_pointer])
                first_pointer += 1
                second_pointer += 1
                print(f"{first_list[first_pointer]} == {second_list[second_pointer]}")

    except IndexError:
        return resulting_list


def lazy_merge_sort_two_arrays(first_list, second_list):
    first = iter(first_list)
    second = iter(second_list)
    resulting_list = []

    value1 = next(first)
    value2 = next(second)
    while True:
        if value1 > value2:
            print(f"{value1} > {value2}")
            yield value2
            try:
                value2 = next(second)
            except StopIteration:
                resulting_list.extend([value1, *first])
                return resulting_list
        elif value1 < value2:
            print(f"{value1} < {value2}")
            yield value1
            try:
                value1 = next(first)
            except StopIteration:
                resulting_list.extend([value2, *second])
                return resulting_list
        else:
            print(f"{value1} == {value2}")
            try:
                yield value1
                value1 = next(first)
                value2 = next(second)
            except StopIteration:
                return resulting_list
