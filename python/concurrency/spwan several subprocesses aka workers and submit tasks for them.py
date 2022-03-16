"""
How to spawn as much workers as you much cpu/cores you have and assign all your
cpu bound tasks to them in turn

https://stackoverflow.com/questions/23816546/how-many-processes-should-i-run-in-parallel
https://stackoverflow.com/questions/8533318/multiprocessing-pool-when-to-use-apply-apply-async-or-map
"""

import multiprocessing as mp
from time import perf_counter

import pandas as pd


def open_file(file):  # the func called in child processes
    print(f'Opening {file}...')
    df = pd.read_excel(file)
    print(f'Done with {file}...')
    return df


def multi_add(files):
    num_workers = mp.cpu_count() // 2
    print(f'{num_workers=}')

    pool = mp.Pool(num_workers)

    results = [pool.apply_async(open_file, args=(file,)) for file in files]

    pool.close()
    pool.join()

    for res in results:
        res = res.get()
        print(res.head(n=5))


if __name__ == '__main__':
    print('Program started...')

    files = [f'{i}.xlsx' for i in range(1, 11)]

    start = perf_counter()
    multi_add(files)

    finish = perf_counter()
    print(f'Opened {len(files)} in {round(finish - start, 2)} seconds')
