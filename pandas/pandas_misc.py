

def test_lpu_match():
    # an example of iteration through pandas dataframe

    # path_to_base = join(ROOT_FOLDER, 'data/allianz/ЦЛ МОСКВА открытые.xlsx')
    # df = pd.read_excel(path_to_base)
    # df['rcode'] = df['risks_detected'].map(ap._risk_to_rcode)
    # with open('lpu_search_result.txt', 'w') as outp:
    df = pd.read_excel('vesp_20191511.xlsx')

    vf = VespFinder()

    for row in df.itertuples():

        lpu_code = str(row.True_code)

        if lpu_code.strip().lower() == 'нет договора':
            # logger.debug('нет договора')
            continue

        logger.debug('lpu code to search: %s', lpu_code)
        vesp = Vesp(lpu_code=lpu_code,
                    rcode=vf._risk_to_rcode(row.risk),
                    age=row.age,
                    pricelist_db=vf._PRICELIST_DB)
        result = vesp.get()
        logger.debug(getattr(result, 'df', result))


def check_column_eq():
    df_old
    df_new =
    for i in range(df_old.shape[1]):
        if not np.all(df_old.iloc[:, i] == df_new.iloc[:, i]):
            print(f'old: {df_old.columns[i]}, new: {df_new.columns[i]}')
            print(np.where(df_new.iloc[:, i] != df_old.iloc[:, i]))
            # print(df_new.iloc[:, i])


def _make_unique_ids_by_other_combinations_of_another_unique_values()
    df = pd.read_excel('vsk_2019_12_05.xlsx')

    def make_identifier(df):
        str_id = df.apply(lambda x: '_'.join(map(str, x)), axis=1)
        return pd.factorize(str_id)[0]

    df['unique_id'] = make_identifier(df[['Дата рождения','Пол', 'Код ЛПУ']])

    df = df.sort_values(by='unique_id')
    df.to_excel('vsk_preprocessed_2019_12_05.xlsx')
    print('Done')