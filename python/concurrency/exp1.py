import time
import multiprocessing as mp

import pandas as pd

start_point = time.perf_counter()
df = pd.read_excel("11.xlsx")
print(f"Opening excel took {time.perf_counter() - start_point} seconds")
df = df.sort_values(by=["Unnamed: 0"])

num_workers = mp.cpu_count() // 2
print(f"{num_workers=}")
rows_in_each_df = df.shape[0] // num_workers
print(f"{rows_in_each_df=}")


def apply_regex(val):
    t = 1000**10000
    if "Прием" in val:
        return 1
    return 0


def apply_smth_to_df(df):
    df["new_column"] = df["SERVICE_NAME"].apply(apply_regex)
    return df


#
start_pnt = time.perf_counter()

# apply_smth_to_df(df)

pool = mp.Pool(num_workers)


i = 0
queue = []

for _ in range(num_workers):
    df_part = df.iloc[i : i + rows_in_each_df]
    i += rows_in_each_df
    queue.append(pool.apply_async(apply_smth_to_df, args=(df_part,)))

first_df = queue[0].get()
for df in queue[1:]:
    first_df = first_df.append(df.get())

print(first_df)
print(f"Applying took took {time.perf_counter() - start_pnt} seconds")
pool.close()
