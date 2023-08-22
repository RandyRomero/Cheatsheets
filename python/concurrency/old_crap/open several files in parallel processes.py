from multiprocessing import Queue, Process
from time import perf_counter

import pandas as pd


def open_file(queue, file):  # the func called in child processes
    print(f"Opening {file}...")
    df = pd.read_excel(file)
    queue.put(df)
    print(f"Done with {file}...")


def multi_add(files):  # spawns child processes
    q = Queue()
    processes = []
    dframes = []

    for file in files:
        p = Process(target=open_file, args=(q, file))
        processes.append(p)
        p.start()
    for _ in processes:
        print("Getting results...")
        df = q.get()  # will block
        dframes.append(df)
    for p in processes:
        print("Killing processes...")
        p.join()
    return dframes


if __name__ == "__main__":
    print("Program started...")
    filepaths = (
        "sogaz_0218_LM_0045D_023.20.02_results.xlsx",
        "sogaz_0218_LM_0045D_044_results.xlsx",
        "sogaz_0619_LM_000040D_013_results.xlsx",
    )

    start = perf_counter()
    dfs = multi_add(filepaths)
    finish = perf_counter()
    print(f"Opened {len(filepaths)} in {round(finish - start, 2)} seconds")
