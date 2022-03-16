import array
from time import perf_counter

my_list = list(range(10000000))
# print(my_list)


# for i in range(100):
#     my_sum = 0
#     for item in my_list:
#         my_sum += item
#     print(i)

# start = perf_counter()
# for i in range(100):
#     sum(my_list)
# print(perf_counter() - start)

my_array = array.array("i", my_list)
start = perf_counter()
for i in range(100):
    sum(my_array)
    print(i)
print(perf_counter() - start)

# timeit("my")