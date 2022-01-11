#!/usr/bin/python3
import os
import sys
import csv
from src.util.csv_writer import CsvWriter


def print_usage(executable_name, error_msg=None):
    print(f'Usage: {executable_name}')
    print()
    if error_msg is not None:
        print(f'Error: {error_msg}')
    sys.exit(1)


def main(argv):
    file_prefixes = ['Gram_Sevak_Survey_', 'Group_Survey_', 'Notable_Survey_', 'Sarpanch_Survey_', 'Upa_Sarpanch_Survey_']
    for file_prefix in file_prefixes:
        file_suffixes = ['1', '2', '2_bis', '3', '4']
        for file_suffix in file_suffixes:
            file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_corrected/{file_prefix}{file_suffix}.csv'
            if not os.path.isfile(file_path):
                raise Exception(f'{file_path} is not valid ')
            result_lines = []
            with open(file_path, 'r', encoding='utf-8') as original:
                lines = csv.reader(original, delimiter=',')
                skip_first = True
                for line in lines:
                    if skip_first is True:
                        skip_first = False
                        for idx, col in enumerate(line):
                            line[idx] = col.lower().replace('gps-', 'gps')
                    result_lines.append(line)
            CsvWriter.write(file_path, result_lines)


if __name__ == '__main__':
    main(sys.argv)
