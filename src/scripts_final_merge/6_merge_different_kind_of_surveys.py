#!/usr/bin/python3
import os
import sys
import pandas as pd


def main(argv):
    file_nicknames = ['r_', 's_', 'gs_', 'g_', 'u_']
    file_prefixes = ['Sampling', 'Sarpanch_Survey_', 'Gram_Sevak_Survey_', 'Group_Survey_', 'Upa_Sarpanch_Survey_']
    output_name = 'Reservation_Sarpanch_Gram_Sevak_Group_Upa_Sarpanch.csv'

    file_nicknames = ['r_', 's_', 'n_']
    file_prefixes = ['Sampling', 'Sarpanch_Survey_', 'Notable_Survey_']
    output_name = 'Reservation_Sarpanch_Notable_long.csv'

    # file_nicknames = ['r_', 's_', 'n_']
    # file_prefixes = ['Sampling', 'Sarpanch_Survey_', 'Notable_Survey_Wide']
    # output_name = 'Reservation_Sarpanch_Notable.csv'

    all_dataframes = []
    for idx, file_prefix in enumerate(file_prefixes):
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_merged/{file_prefix}.csv'
        if not os.path.isfile(file_path):
            raise Exception(f'{file_path} is not valid ')
        try:
            df = pd.read_csv(file_path, dtype=str)
            df = df.add_prefix(file_nicknames[idx])
            all_dataframes.append(df)
        except Exception as exp:
            raise Exception(f'Failed for {file_path}: {str(exp)}')
    final_df = None
    for idx, df in enumerate(all_dataframes):
        if final_df is None:
            final_df = df
            continue
        final_df = pd.merge(final_df, df, how='inner', left_on=[f'{file_nicknames[idx - 1]}villageid'], right_on=[f'{file_nicknames[idx]}villageid'])
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_merged/{output_name}'
    final_df.to_csv(path_or_buf=file_path, index=False)


if __name__ == '__main__':
    main(sys.argv)