def counting_sort(
    original_list: list[int], min_value: int, max_value: int
) -> list[int]:
    """Performs sorting of the given array using counting sort."""

    offset = min_value - 0  # in case original list starts with value bigger than zero

    auxiliary_array = [0] * (max_value - min_value + 1)
    output_array = [0] * len(original_list)

    # count how many times each value occurs in the original array
    for value in original_list:
        auxiliary_array[value - offset] += 1

    y = 0
    for i in range(len(auxiliary_array)):
        for _ in range(auxiliary_array[i]):
            output_array[y] = i + min_value
            y += 1
    return output_array


if __name__ == "__main__":
    my_list = [1, 4, 1, 2, 7, 5, 2]

    sorted_list = sorted(my_list)
    sorted_by_counting_sort = counting_sort(my_list, 1, 7)

    print(sorted_by_counting_sort)

    assert (
        sorted_by_counting_sort == sorted_list
    ), f"Expected result: {sorted_list},\nactual result: {sorted_by_counting_sort}"
    print("succes!")
