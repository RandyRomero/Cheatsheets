"""
Задача: в файле находятся все возможные телефонные номера в виде +79XXXXXXXXX (11 цифр) в произвольном порядке.
Нужно написать программу сортирующую эти номера и сохраняющие в новый файл.
Программа должна работать максимально быстро (наряду с кодом нужно предоставить
замер по времени выполнения сортировки файла содержащего все записи).

Дополнительно: написать программу для генерации исходного файла.
"""



import os
import random
from time import perf_counter


NUMBERS_FILE_PATH = os.getenv('NUMBERS_FILE_PATH', "numbers_file.txt")
SHUFFLED_FILE_PATH = os.getenv('SHUFFLED_FILE_PATH', "numbers_file.txt")

ONE_MILLION = 1000000

START_NUMBER = int(os.getenv('START_NUMBER', 79000000000))
STOP_NUMBER = int(os.getenv('STOP_NUMBER', 80000000000))

PRINT_EVERY = int(os.getenv('PRINT_EVERY', ONE_MILLION))
READ_LINES_LIMIT = int(os.getenv('PRINT_EVERY', 250 * ONE_MILLION))


def create_phone_numbers_file(filepath: str) -> None:
    """
    Creates file with all Russian mobile phone numbers.

    Looks like:
    +79000000000
    +79000000001
    +79000000002
    ...
    +79999999999
    """
    with open(filepath, "w") as outfile:
        for number in range(START_NUMBER, STOP_NUMBER):
            if number % PRINT_EVERY == 0:
                print(f"Current number is {number}")
            outfile.write(f"+{number}\n")


def get_line_length(filepath: str) -> int:
    """Count lines in a given file."""
    with open(filepath, 'r') as infile:
        lines_number = sum(1 for _ in infile)

    return lines_number

# def read_in_chunks(file_object, chunk_size=1024):
#     while True:
#         data = file_object.read(chunk_size)
#         if not data:
#             break
#         yield data



def shuffle_file_in_chunks(
        ordered_file_path: str,
        shuffled_file_path: str,
        read_lines_limit: int = 1,
) -> None:

    with open(ordered_file_path, "r") as ordered_file:
        with open(shuffled_file_path, "w") as shuffled_file:
            lines = []
            i = 0

            # read a chuck -> shuffle chunk -> store to file (buffer) -> read the next chunk
            while True:
                i += 1
                line = ordered_file.readline()
                lines.append(line)
                if i % read_lines_limit == 0:
                    random.shuffle(lines)
                    for l in lines:
                        shuffled_file.write(l)
                    lines[:] = []
                if line == "":
                    break


if __name__ == '__main__':
    now = perf_counter()
    if not os.path.exists(NUMBERS_FILE_PATH):
        create_phone_numbers_file(NUMBERS_FILE_PATH)
        print(f"There are {get_line_length(NUMBERS_FILE_PATH)} lines.")

    shuffle_file_in_chunks(NUMBERS_FILE_PATH, SHUFFLED_FILE_PATH, READ_LINES_LIMIT)
    print(f"There are {get_line_length(SHUFFLED_FILE_PATH)} lines.")

    print("done")
    print(perf_counter() - now)


# import random
# from time import perf_counter
#
# total_num = 1000000000
#
# # def powerset(iterable):
# #     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
# #     s = list(iterable)
# #     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
#
#
# numbers = set()
#
#
#
# def gen_phone_numbers():
#     my_list = [False for _ in range(total_num)]
#
#     with open("numbers_file.txt", "w+") as outfile:
#
#         while len(numbers) < total_num:
#             new_num = int(random.random() * 1000000000)
#             if my_list[new_num]:
#                 continue
#             outfile.write(f"+79{}")
#             # numbers.add(new_num)
#
#             # my_list[new_num] = True
#
#
#
#     # a = array.array('i', range(total_num))
#     # print(len(a))
# #
# # def gen_phone_numbers2():
#     # i = 0
#     # while len(numbers) < 1000000000:
#     #     new_num = int(random.random() * 1000000000)
#     #     if new_num in numbers:
#     #         numbers.add(new_num + 1)
#     #         continue
#     #     numbers.add(new_num)
#     #     # numbers.add(int(random.random() * 1000))
#     #     i += 1
#     #
#     # print(i)
#     # print(len(numbers))
#     # print(numbers)
#
#     # numbers = list(range(total_num + 1))
#     # shuffle(numbers)
#     # for number in numbers:
#     #     f"+79{number}"
#     # # shuffle(range(1000000000)):
#
#     # with open("phone_numbers.txt", "w") as phone_numbers_file:
