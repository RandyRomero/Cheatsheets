### What are our options to merge sorted lists/iterables in Python?

Either `iterative k-way merge` or `heapq.merge()` or `sorted(left + right)`

question id: aaa6fa31-d709-4cff-a768-63c42b65e0d


### Compare performance of the 3 options to merge sorted lists/iterables in Python

- `sorted(left + right)` is always 2-8 times faster on different range of inputs and input length,
but requires O(n) memory (it has to create a list in order to sort it)

- `iterative k-way merge` is ~2 faster than `heapq.merge()` on low amount of inputs (k) (up to 3-4)

- the more amount of inputs (k), the faster the `heapq.merge()` than - `iterative k-way merge`, 
but the more items in inputs (n), the less the difference until they are neck to neck

There is some code to check it:
```python
from time import perf_counter
from heapq import merge
print("start")

loop_times = 10
range_length = 1000000
now = perf_counter()
for _ in range(loop_times):
    list(k_way_merge(range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length)))
two_way_merge_time = perf_counter() - now
print(f"It took {two_way_merge_time} seconds to merge {range_length * 2} values with two way merge")

now = perf_counter()
for _ in range(loop_times):
    list(merge(range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length), range(range_length)))
heapq_merge_time = perf_counter() - now
print(f"It took {heapq_merge_time} seconds to merge {range_length * 2} values with heapq.merge()")

now = perf_counter()
for _ in range(loop_times):
    sorted(list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)) + list(range(range_length)))
sorted_time = perf_counter() - now
print(f"It took {sorted_time} seconds to merge {range_length * 2} values with sorter([] + [])")

print()
print(f"Sorted {heapq_merge_time / sorted_time} times faster then heap q merge")
print(f"Sorted {two_way_merge_time / sorted_time } times faster then two-way merge")
```

question id: 5cc28161-c955-4538-84d3-4e2e3654afa4

