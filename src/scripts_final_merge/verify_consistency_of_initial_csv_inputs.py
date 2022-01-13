#!/usr/bin/python3
import os
import sys
import csv


def find_column_position(line, column_name):
    for i, column in enumerate(line):
        if column.strip().lower() == column_name:
            return i
    print(line)
    raise Exception(f'Could find find {column_name}')


def main(argv):

    district_column_name = 'q6'
    villageid_column_name = 'villageid'
    villagename_column_name = 'q1'

    file_prefixes = ['Gram_Sevak_Survey_', 'Group_Survey_', 'Notable_Survey_', 'Sarpanch_Survey_', 'Upa_Sarpanch_Survey_']

    for file_prefix in file_prefixes:
        file_suffixes = ['1', '2', '2_bis', '3', '4']
        for file_suffix in file_suffixes:
            file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/{file_prefix}{file_suffix}.csv'
            if not os.path.isfile(file_path):
                raise Exception(f'{file_path} is not valid ')
            try:
                with open(file_path, 'r', encoding='utf-8') as original:
                    lines = csv.reader(original, delimiter=',')
                    skip_first = True
                    instanceid_column_pos = None
                    instanceid_set = set()
                    for line in lines:
                        if skip_first is True:
                            skip_first = False
                            district_column_pos = find_column_position(line, district_column_name)
                            villageid_column_pos = find_column_position(line, villageid_column_name)
                            villagename_column_pos = find_column_position(line, villagename_column_name)
                            print(f'{district_column_pos}, {villageid_column_pos}, {villagename_column_pos} for {file_prefix}{file_suffix}.csv')
                            instanceid_column_pos = find_column_position(line, 'instanceid')
                            continue
                        instanceid = line[instanceid_column_pos]
                        if instanceid in instanceid_set:
                            print(f'Duplicate {instanceid} inside {file_prefix}{file_suffix}.csv')
                        instanceid_set.add(instanceid)
            except Exception as exp:
                raise Exception(f'Failed for {file_prefix}{file_suffix}.csv : {str(exp)}')


if __name__ == '__main__':
    main(sys.argv)
