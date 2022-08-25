#!/usr/bin/python3
import os
import re
import pandas as pd

from src.scripts_final_merge.utils.columns import COLUMNS


def turn_into_old_format(file_path, new_file_path):
    if not os.path.isfile(file_path):
        raise Exception(f'{file_path} is not valid')
    df = pd.read_csv(file_path, dtype=str)
    expected_columns = [c for c in df.columns]
    print(f'Expecting {len(expected_columns)} columns')
    print(expected_columns)
    print()

    file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/amravati/Gram_Sevak_Survey_Amravati_-_all_versions_-_False_-_2022-07-29-05.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'{file_path} is not valid')
    df = pd.read_csv(file_path, dtype=str)

    df = df.drop('GPS', axis=1)
    df = df.drop('audit_URL', axis=1)
    df = df.drop('NoteConsent', axis=1)
    df = df.drop('Q55_2_a', axis=1)
    df = df.drop('Q55_2_b', axis=1)
    df = df.drop('Q2021_1', axis=1)
    df = df.drop('Q2021_2', axis=1)
    df = df.drop('Q2021_3', axis=1)
    df = df.drop('Q505_URL', axis=1)
    df = df.drop('background-audio_URL', axis=1)
    df = df.drop('__version__', axis=1)
    df = df.drop('_validation_status', axis=1)
    df = df.drop('_notes', axis=1)
    df = df.drop('_status', axis=1)
    df = df.drop('_submitted_by', axis=1)
    df = df.drop('_tags', axis=1)

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

    df['Group_Village_count'] = ''
    df['Q22_1.1'] = ''
    df['Q22_2.1'] = ''
    df['Q22_3.1'] = ''
    df['Q22_4.1'] = ''
    df['Q22_5.1'] = ''
    df['Q22_6.1'] = ''
    df['Q22_7.1'] = ''
    df['Q22_8.1'] = ''
    df['Q22_9.1'] = ''
    df['Q22_10.1'] = ''
    df['Q50_1_1.1'] = ''
    df['Village_Sr_1'] = ''
    df['Q58_1_1'] = ''
    df['Q58_2_1'] = ''
    df['Q58_3_1'] = ''
    df['Q58_4_1'] = ''
    df['Q58_5_1'] = ''
    df['Q58_6_1'] = ''
    df['Q201_1'] = ''
    df['Q58_7_1'] = ''
    df['Q202_1'] = ''
    df['Q203_1'] = ''
    df['Q204_1'] = ''
    df['Q205_1'] = ''
    df['Village_Sr_2'] = ''
    df['Q58_1_2'] = ''
    df['Q58_2_2'] = ''
    df['Q58_3_2'] = ''
    df['Q58_4_2'] = ''
    df['Q58_5_2'] = ''
    df['Q58_6_2'] = ''
    df['Q201_2'] = ''
    df['Q58_7_2'] = ''
    df['Q202_2'] = ''
    df['Q203_2'] = ''
    df['Q204_2'] = ''
    df['Q205_2'] = ''
    df['Village_Sr_3'] = ''
    df['Q58_1_3'] = ''
    df['Q58_2_3'] = ''
    df['Q58_3_3'] = ''
    df['Q58_4_3'] = ''
    df['Q58_5_3'] = ''
    df['Q58_6_3'] = ''
    df['Q201_3'] = ''
    df['Q58_7_3'] = ''
    df['Q202_3'] = ''
    df['Q203_3'] = ''
    df['Q204_3'] = ''
    df['Q205_3'] = ''
    df['Village_Sr_4'] = ''
    df['Q58_1_4'] = ''
    df['Q58_2_4'] = ''
    df['Q58_3_4'] = ''
    df['Q58_4_4'] = ''
    df['Q58_5_4'] = ''
    df['Q58_6_4'] = ''
    df['Q201_4'] = ''
    df['Q58_7_4'] = ''
    df['Q202_4'] = ''
    df['Q203_4'] = ''
    df['Q204_4'] = ''
    df['Q205_4'] = ''
    df['formdef_version'] = ''

    # TODO
    df = df.drop('Q22/1', axis=1)
    df = df.drop('Q22/2', axis=1)
    df = df.drop('Q22/3', axis=1)
    df = df.drop('Q22/4', axis=1)
    df = df.drop('Q22/5', axis=1)
    df = df.drop('Q22/6', axis=1)
    df = df.drop('Q22/7', axis=1)
    df = df.drop('Q22/8', axis=1)
    df = df.drop('Q22/9', axis=1)
    df = df.drop('Q22/10', axis=1)
    df = df.drop('Q50_1/1', axis=1)

    df = df.reindex(columns=expected_columns)

    current_columns = [c for c in df.columns]
    print(f'Currently {len(current_columns)} columns')
    print(current_columns)

    print('missing matches for')
    for column in df.columns:
        if column not in expected_columns:
            print(f"df = df.drop('{column}', axis=1)")
    print('\nmissing')
    for column in expected_columns:
        if column not in df.columns:
            print(f"df['{column}'] = ''")

    if expected_columns != current_columns:
        raise Exception('Columns are not matching')

    df.to_csv(path_or_buf=new_file_path, index=False)


def main():
    file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/ahmednagar/Gram_Sevak_Survey_WIDE.csv'
    new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/Gram_Sevak_Survey_5.csv'
    turn_into_old_format(file_path, new_file_path)

    file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/amravati/Gram_Sevak_Survey_Amravati_-_all_versions_-_False_-_2022-07-29-05.csv'
    new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/Gram_Sevak_Survey_6.csv'
    turn_into_old_format(file_path, new_file_path)


if __name__ == '__main__':
    main()
