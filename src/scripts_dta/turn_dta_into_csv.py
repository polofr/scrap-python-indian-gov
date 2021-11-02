#!/usr/bin/python3
import os
import sys
import pandas

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')


def print_usage(executable_name, error_msg=None):
    print(f'Usage: {executable_name}')
    print()
    if error_msg is not None:
        print(f'Error: {error_msg}')
    sys.exit(1)


def main(argv):
    filenames = ['Gram_Sevak_Survey_Merged_20210904', 'Group_Survey_Merged_20210824', 'Notable_Survey_20201026', 'Sarpanch_Survey_Merged_20210824', 'Upa_Sarpanch_Survey_Merged_20210824']
    for filename in filenames:
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/dta_files/{filename}.dta'
        new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/{filename}.csv'
        if not os.path.isfile(file_path):
            print(f'Could not find {file_path}')
            continue
        data = pandas.io.stata.read_stata(file_path)
        data.to_csv(new_file_path)


if __name__ == '__main__':
    main(sys.argv)
