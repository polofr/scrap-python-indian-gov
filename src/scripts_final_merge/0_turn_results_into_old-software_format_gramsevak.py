#!/usr/bin/python3
import os
import re
import pandas as pd

from src.scripts_final_merge.utils.columns import COLUMNS


def turn_into_old_format(expected_file_path, file_path, new_file_path):
    if not os.path.isfile(expected_file_path):
        raise Exception(f'{expected_file_path} is not valid')
    df = pd.read_csv(expected_file_path, dtype=str)
    expected_columns = [c for c in df.columns]
    print(f'\nExpecting {len(expected_columns)} columns as per {expected_file_path.split("/")[-1]}')
    print(expected_columns)
    print()

    if not os.path.isfile(file_path):
        raise Exception(f'{file_path} is not valid')
    df = pd.read_csv(file_path, dtype=str)

    # TODO because they are duplicated Q22_1 and Q22/1, we prefer to keep Q22/1
    df = df.drop('Q22_1', axis=1)
    df = df.drop('Q22_2', axis=1)
    df = df.drop('Q22_3', axis=1)
    df = df.drop('Q22_4', axis=1)
    df = df.drop('Q22_5', axis=1)
    df = df.drop('Q22_6', axis=1)
    df = df.drop('Q22_7', axis=1)
    df = df.drop('Q22_8', axis=1)
    df = df.drop('Q22_9', axis=1)
    df = df.drop('Q22_10', axis=1)
    df = df.drop('Q50_1_1', axis=1)

    for old_column in df.columns:
        matches = re.match(r'^Note[0-9]+$', old_column)
        if matches:
            df = df.drop(old_column, axis=1)
            continue
        new_column = COLUMNS.get(old_column)
        if new_column:
            if new_column in df.columns:
                print(f'column {new_column} already exists')
            df = df.rename({old_column: new_column}, axis=1)
            continue
        matches = re.match(r'^Q[_0-9]+/[0-9]+$', old_column)
        if matches:
            new_column = old_column.replace('/', '_')
            if new_column in df.columns:
                print(f'column {new_column} already exists 2')
                continue  # TODO
            df = df.rename({old_column: new_column}, axis=1)
            continue

    df = df.reindex(columns=expected_columns)

    current_columns = [c for c in df.columns]
    print(f'Currently {len(current_columns)} columns in {file_path.split("/")[-1]}')
    print(current_columns)

    print('columns that should be deleted')
    for column in df.columns:
        if column not in expected_columns:
            print(f"df = df.drop('{column}', axis=1)")
    print('columns that should be added')
    for column in expected_columns:
        if column not in df.columns:
            print(f"df['{column}'] = ''")

    if expected_columns != current_columns:
        raise Exception('Columns are not matching')

    df.to_csv(path_or_buf=new_file_path, index=False)


def main():
    expected_file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Gram_Sevak_Survey_Merged_20210904.csv'
    file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/amravati/Gram_Sevak_Survey_Amravati_-_all_versions_-_False_-_2022-07-29-05.csv'
    new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/Gram_Sevak_Survey_5.csv'
    turn_into_old_format(expected_file_path, file_path, new_file_path)

    file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/aurangabad/Gram_Sevak_Survey_-_all_versions_-_False_-_2022-04-01-05.csv'
    new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/Gram_Sevak_Survey_6.csv'
    turn_into_old_format(expected_file_path, file_path, new_file_path)


if __name__ == '__main__':
    main()
