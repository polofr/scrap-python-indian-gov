#!/usr/bin/python3
import os
import sys
import pandas as pd


def main(argv):
    file_prefixes = ['Gram_Sevak_Survey_', 'Group_Survey_', 'Notable_Survey_', 'Sarpanch_Survey_', 'Upa_Sarpanch_Survey_']
    for file_prefix in file_prefixes:
        file_suffixes = ['1', '2', '2_bis', '3', '4']
        all_dataframes = []
        for file_suffix in file_suffixes:
            file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_corrected/{file_prefix}{file_suffix}.csv'
            if not os.path.isfile(file_path):
                raise Exception(f'{file_path} is not valid')
            try:
                df = pd.read_csv(file_path, dtype=str)  # nrows=5,
                all_dataframes.append(df)
            except Exception as exp:
                raise Exception(f'Failed for {file_path}: {str(exp)}')
        final_dataframe = pd.concat(all_dataframes, axis=0, ignore_index=True)
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_merged/{file_prefix}.csv'
        final_dataframe.to_csv(path_or_buf=file_path, index=False)


if __name__ == '__main__':
    main(sys.argv)
