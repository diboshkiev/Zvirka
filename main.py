import os.path
import numpy as np
from startup_module import general_settings
import pandas


def verify():

    input_file_exists = file_exists(general_settings.input_polk)

    if not input_file_exists:
        # print("{{-------------------------------------------------")
        print('{{ Input file not found!!!')
        print('Operation aborted!!!')
        print("-------------------------------------------------}}")
        return

    excel_polk_df = pandas.read_excel(general_settings.input_polk, sheet_name=general_settings.sheet_polk,
                                      header=general_settings.header_row_polk, names=None,
                                      index_col=None, usecols=general_settings.use_cols_polk)

    excel_4bo_df = pandas.read_excel(general_settings.input_4bo, sheet_name=general_settings.sheet_4bo,
                                     header=general_settings.header_row_4bo, names=None,
                                     index_col=None, usecols=general_settings.use_cols_4bo)

    # rename columns
    excel_polk_df.columns = general_settings.use_cols_polk_names
    excel_4bo_df.columns = general_settings.use_cols_4bo_names

    # remove Nan indexes
    excel_polk_df.replace([np.inf, -np.inf, pandas.NA, pandas.NaT, "", '', ], np.nan, inplace=True)
    excel_4bo_df.replace([np.inf, -np.inf, pandas.NA, pandas.NaT, "", ''], np.nan, inplace=True)


    excel_polk_df[['PIB', 'ZvFact']].astype(str)
    excel_4bo_df[['PIB', 'ZvFact']].astype(str)

    # set new values for empty strings
    excel_polk_df['PIB'] = excel_polk_df['PIB'].fillna('**empty**')
    excel_4bo_df['PIB'] = excel_4bo_df['PIB'].fillna('**empty**')
    excel_polk_df['ZvFact'] = excel_polk_df['ZvFact'].fillna('**empty**')
    excel_4bo_df['ZvFact'] = excel_4bo_df['ZvFact'].fillna('**empty**')


    excel_polk_df['NSht']  = excel_polk_df['NSht'] .fillna(-1)
    excel_4bo_df['NSht']  = excel_4bo_df['NSht'] .fillna(-1)

    excel_polk_df = excel_polk_df.query("NSht != -1")
    excel_4bo_df = excel_4bo_df.query("NSht != -1")


    # set indexes NSht
    excel_polk_df.set_index('NSht', inplace=True)
    excel_4bo_df.set_index('NSht', inplace=True)

    # set upper
    excel_polk_df['PIB'] = excel_polk_df['PIB'].str.title()
    excel_4bo_df['PIB'] = excel_4bo_df['PIB'].str.title()
    excel_polk_df['ZvFact'] = excel_polk_df['ZvFact'].str.title()
    excel_4bo_df['ZvFact'] = excel_4bo_df['ZvFact'].str.title()

    # excel_polk_df = excel_polk_df.head(10)
    # excel_4bo_df = excel_4bo_df.head(10)

    excel_polk_df.to_excel("output.xlsx", sheet_name='Sheet_name_1')
    excel_4bo_df.to_excel("output_4.xlsx", sheet_name='Sheet_name_1')

    # marge dataframes
    df_differences = pandas.merge(excel_polk_df, excel_4bo_df, how="outer", on=["NSht"], suffixes=("_Core", "_Local"))
    df_differences.to_excel('diff_s.xlsx', sheet_name='4bo')

    df_differences = df_differences.query("(PIB_Core != PIB_Local) or  (ZvFact_Core != ZvFact_Local)")
    #df_differences = df_differences.query("PIB_Core != PIB_Local")
    df_differences.to_excel('diff_s.xlsx', sheet_name='4bo')

    #print(excel_4bo_df)
    #print(excel_4bo_df['PIB'] + " " + str(type(excel_4bo_df['PIB'])))
    print(excel_4bo_df['PIB']+" "+str(excel_4bo_df['PIB'].isna()))
    print(str(type(excel_4bo_df['PIB'])))

    #print(df_differences)


def file_exists(file_name):
    return os.path.exists(file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    verify()
