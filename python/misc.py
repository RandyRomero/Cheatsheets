from typing import NamedTuple


class TestCase(NamedTuple):
    nums1: list[int]
    nums2: list[int]
    output: list[int]


test_cases = [
    TestCase(nums1=[12,28,46,32,50], nums2=[50,12,32,46,28], output=[1,4,3,2,0]),
    TestCase(nums1=[84,46], nums2=[84,46], output=[0, 1]),
]


def get_list(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    You are given two integer arrays nums1 and nums2 where nums2
     is an anagram of nums1. Both arrays may contain duplicates.

    Return an index mapping array mapping from nums1 to nums2 where 
    mapping[i] = j means the ith element in nums1 appears in nums2 at index j. 
    If there are multiple answers, return any of them.

    An array a is an anagram of an array b means b is made by randomizing the 
    order of the elements in a.
    """

    num_to_index = {}
    for i, num in enumerate(nums2):
        num_to_index[num] = i

    output = []
    for num in nums1:
        output.append(num_to_index[num])

    return output


for test_case in test_cases:
    output = get_list(test_case.nums1, test_case.nums2)
    assert (
        output == test_case.output
    ), (f"actual_result: {output}",
        f"expected_result: {test_case.output},"
        f"nums1: {test_case.nums1},"
        f"nums2: {test_case.nums2}")

print("success!")
