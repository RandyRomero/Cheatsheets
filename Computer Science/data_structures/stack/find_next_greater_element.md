### How to find next greater element? In theory, no code


Having an array of numbers - return the corresponding array with the next
greater element for each original number.

- For an array, the rightmost element always has the next greater element as -1.
- For an array that is sorted in decreasing order, all elements have the next greater element as -1.

```
Example 1:
[4, 5, 2, 25] => [5, 25, 25, -1]

Example 2:
[13, 7, 6, 12] => [-1, 12, 12, -1]
```

The solution should be not worse than O(n) in terms of time and space complexity.

answer:
In order to traverse the array only once, we need to use a monotonic stack and
traverse the list from the right to the left.

Monotonic stack - it is a stack where you can only add a new value if it is lower/higher than the
value on top of the stack. For decreasing monotonic stack in order to add a new value it should
be lower than the value on top of the stack and vice versa for the increasing monotonic stack.
However, how does it help us to find the next greater element in just one path?

First, we need to  create an output array and fill it with -1, so if we don't find the next greater
element (NGE), we just left the value as-is.

Then we will traverse the original list from right to left, adding each element to the stack.
However, we should first check if it is lower than the element on top of the stack or not.
If it is lower - we just add it to the stack, and also for this element the NGE will obviously be 
the value on top of the stack.

If the current value from the original array is bigger than the value on top of the stack,
we pop the top value from the stack. And we will continue popping the values from the stack
until we find one that is greater than the current value from the original array. That is
the NGE for the current value from the original list.

For example, let's take [4, 5, 2, 25].
The stack is empty and we just add 25. There is no NGE for the rightmost element anyway,
so we left the default value in the output array - -1.

We take the next value, 2, and compare it to 25. 2 is less than 25, so we just 
add it to the stack and put to the output array that 25 is the NGE for the 2. 
We also put 2 on the stack. The stack now is [2, 25].

We take the next value, 5, and its greater than the value on top of the stack, 2, so we pop 2 and compare 
5 to the next value - 25. 25 is greater, so 25 is the NGE to 5. We also add 5 to the stack, so the stack now is
[5, 25].

We take the next value, 4, and compare it to the 5. 5 is greater than 4, so 5 is the NGE for the 4.
We have finished.

Useful links:
https://www.geeksforgeeks.org/next-greater-element/
https://www.youtube.com/watch?v=dtiBmmIPR0E


question id: 30afc047-746d-4a47-8fde-7e4c38c5752a


### How to find next greater element? Coding task

https://www.geeksforgeeks.org/next-greater-element/

Having an array of numbers - return the corresponding array with the next
greater element for each original number.

- For an array, the rightmost element always has the next greater element as -1.
- For an array that is sorted in decreasing order, all elements have the next greater element as -1.

```
Example 1:
[4, 5, 2, 25] => [5, 25, 25, -1]

Example 2:
[13, 7, 6, 12] => [-1, 12, 12, -1]
```

The solution should be not worse than O(n) in terms of time and space complexity.

Template:
```python
from typing import NamedTuple


class TestCase(NamedTuple):
    nums: list[int]
    result: list[int]


test_cases = [
    TestCase(nums=[4, 5, 2, 25], result=[5, 25, 25, -1]),
    TestCase(nums=[13, 7, 6, 12], result=[-1, 12, 12, -1]),
]


def find_next_greater_element(nums: list[int]) -> list[int]:
    """For each number in the given list the function returns the next greater element."""
    pass


for test_case in test_cases:
    result = find_next_greater_element(test_case.nums)
    assert result == test_case.result, (
        f"actual_result: {result}",
        f"expected_result: {test_case.result}," f"nums: {test_case.nums}",
    )

print("success!")
```

answer:

Using monotonic decreasing stack and traversing the list from the right to the
left, we can achive the result in just one path.

More about monotonic stack here:
https://www.youtube.com/watch?v=dtiBmmIPR0E


```python
from typing import NamedTuple


class TestCase(NamedTuple):
    nums: list[int]
    result: list[int]


test_cases = [
    TestCase(nums=[4, 5, 2, 25], result=[5, 25, 25, -1]),
    TestCase(nums=[13, 7, 6, 12], result=[-1, 12, 12, -1]),
]


def find_next_greater_element(nums: list[int]) -> list[int]:
    """For each number in the given list the function returns the next greater element."""
    stack: list[int] = []
    len_nums = len(nums)
    output = [-1] * len_nums
    for i in range(len_nums - 1, -1, -1):
        current_number = nums[i]
        while stack and current_number > stack[-1]:
            stack.pop()
        if stack:
            output[i] = stack[-1]
        stack.append(current_number)

    return output


for test_case in test_cases:
    result = find_next_greater_element(test_case.nums)
    assert result == test_case.result, (
        f"actual_result: {result}",
        f"expected_result: {test_case.result}," f"nums: {test_case.nums}",
    )

print("success!")
```

question id: 2f0e1068-2555-4f16-bf5f-e88ae0e407d9