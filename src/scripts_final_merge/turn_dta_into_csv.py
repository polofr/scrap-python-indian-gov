#!/usr/bin/python3
import os
import sys
import pandas


def main(argv):
    filenames = ['Gram_Sevak_Survey_20201026', 'Group_Survey_20201026', 'Notable_Survey_20201026', 'Sarpanch_Survey_20101026', 'Upa_Sarpanch_Survey_20201026']
    for filename in filenames:
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/dta_files/{filename}.dta'
        new_file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/{filename}.csv'
        if not os.path.isfile(file_path):
            print(f'Could not find {file_path}')
            continue
        data = pandas.io.stata.read_stata(file_path)
        data.to_csv(new_file_path)


if __name__ == '__main__':
    main(sys.argv)
