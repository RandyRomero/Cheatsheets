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


def groupby_unique() -> None:
    """
    Find if a value within one particular column has more than one unique value
    in another column of this dataframe. For example, find if there are people
    from the same city. Or if any value that should have only one unique
    value has more than one

    :return: None

    question number: 3e713c33-9c49-488c-a1cf-b104a5fd1af2

    """

    df = pd.DataFrame({'Name': ['Corey', 'Harrison', 'Michael', 'David'],
                       'City': ['Vancouver',
                                'Miami',
                                'Portland',
                                'Miami']})

    # your code here

    # output: True

def groupby_unique_filter() -> None:
    """
    Make a new df from the other one if in the other one there are some values
    within a specific column that have more than one (or N) unique values
    in the other column. For example, group people by city. Or find rows
    where insured has more than one birthday due to corrupt data

    question number: 587ad19f-711c-40db-bc49-e2198328bd17

    """

    df = pd.DataFrame({'Name': ['Corey', 'Harrison', 'Michael', 'David'],
                       'City': ['Vancouver',
                                'Miami',
                                'Portland',
                                'Miami']})

    # your code here

    """
    output
    
    1    Harrison
    3       David
    Name: Name, dtype: object
    """

