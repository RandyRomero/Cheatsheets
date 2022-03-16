"""
How to start several task as several processes if tasks are cpu bound, if
number of tasks is less than number of cores of your cpu, if you need to get
the result back

https://www.youtube.com/watch?v=fKl2JW_qrso&list=WL&index=5&t=0s
"""

from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

import pandas as pd


def open_file(file):  # the func called in child processes
    print(f'Opening {file}...')
    df = pd.read_excel(file)
    print(f'Done with {file}...')
    return df


def multi_add(files):
    with ProcessPoolExecutor() as executor:
        results = executor.map(open_file, files)

    for res in results:
        print(res.head(n=5))


def main():
    print('Program started...')
    files = [f'{i}.xlsx' for i in range(1, 9)]

    start = perf_counter()
    multi_add(files)
    finish = perf_counter()
    print(f'Opened {len(files)} in {round(finish - start, 2)} seconds')


if __name__ == '__main__':
    main()

