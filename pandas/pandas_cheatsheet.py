import pandas as pd


def print_specific_columns(df):
    print(df[['date', 'name']])


def main():
    df = pd.read_excel('smartphones.xlsx')
    print_specific_columns(df)


if __name__ == '__main__':
    main()
