import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

df_smartphones = pd.read_excel('smartphones.xlsx')


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

    # your code here...


def foo(df: pd.DataFrame) -> None:
    print(df.groupby('date')['name'].nunique().sort_values(ascending=False))

