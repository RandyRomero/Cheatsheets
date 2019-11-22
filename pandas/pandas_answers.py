import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

df_smartphones = pd.read_excel('smartphones.xlsx')


def print_specific_columns(df):
    """
    example of output:

          date                                         name
    0  2019-06-19                Xiaomi Mi 9T (Snapdragon 730)
    1  2019-06-17             Samsung Galaxy M20 (Exynos 7904)
    2  2019-06-12          OPPO Reno 10x zoom (Snapdragon 855)
    3  2019-06-10                           Realme C2 (MT6762)


    choose one from these
    ['date', 'name', 'all cores', 'one core', 'total score']

    question number: 3a72ea3f-47bf-473d-bc0e-aa075b21ffdb
    """

    print(df[['date', 'name']])


print_specific_columns(df_smartphones)


def drop_rows_with_nan_values(df: pd.DataFrame) -> None:
    """
    ....and save rows which were dropped to show them

    remove rows if there is a nan value in a specified column and keep to df -
    rows without nan values and rows only with nan values (for example to show
    how many them there are)

    :param df: some typical dataframe
    :return: None

    question number: '2e3368bf-1631-4a5c-a988-32805954c4e2'

    """
    # preparing (make some columns contain nan values)
    df_with_nan = df.copy(deep=True)
    df_with_nan[df_with_nan[['all cores', 'one core',
                             'total score']] < 1000] = pd.np.nan

    # Remove_rows_with_missing_values
    # P.S. axis=0 means to delete rows (not columns)
    # P.S2. subset lets you specify which columns to check for nan
    # (instead of all columns)
    columns_to_check = ['all cores', 'one core', 'total score']
    na_free = df_with_nan.dropna(axis=0, subset=columns_to_check)

    # optionally:
    # save rows which were dropped to show them
    only_na = df_with_nan[~df_with_nan.index.isin(na_free.index)]

    print(f'{only_na.shape[0]} rows were dropped because they contain empty '
          f'values in columns: {", ".join(columns_to_check)}. '
          f'There these rows are:\n')

    print(only_na)


def get_series_of_unique_values_by_columns(df: pd.DataFrame) -> None:
    print(df.nunique())


def get_number_of_unique_values(df: pd.DataFrame) -> None:
    print(df['name'].nunique())


def print_series_containing_counts_of_unique_values(df: pd.DataFrame) -> None:
    print(df['date'].value_counts())


def print_all_column_names(df: pd.DataFrame) -> None:
    print(list(df))


def foo(df: pd.DataFrame) -> None:
    print(df.groupby('date')['name'].nunique().sort_values(ascending=False))

