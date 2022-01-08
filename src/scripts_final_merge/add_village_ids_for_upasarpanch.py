#!/usr/bin/python3
import os
import sys
import csv
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')


def print_usage(executable_name, error_msg=None):
    print(f'Usage: {executable_name}')
    print()
    if error_msg is not None:
        print(f'Error: {error_msg}')
    sys.exit(1)


def find_column_position(line, column_name):
    for i, column in enumerate(line):
        if column.strip().lower() == column_name:
            return i
    print(line)
    raise Exception(f'Could find find {column_name}')


def format_first_line(line):
    first_line = []
    for column in line:
        column = column.strip().lower().replace('-', '').replace('_', '')
        first_line.append(column)
    return first_line


def find_village_id(line):
    first_line = []
    for column in line:
        column = column.strip().lower().replace('-', '').replace('_', '')
        first_line.append(column)
    return first_line


def main(argv):
    district_column_name = 'q6'
    villageid_column_name = 'villageid'
    villagename_column_name = 'q1'

    instanceid_set = {}

    files_with_ids = [
        'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/ahmednagar/Upa Sarpanch Survey_WIDE.csv',
        'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/ahmednagar/Upa Sarpanch Survey_WIDE (1).csv',
        'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Upa_Sarpanch_Survey_Merged_20210824.csv'
    ]
    for file_with_ids in files_with_ids:
        with open(file_with_ids, 'r', encoding='utf-8') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            district_column_pos = None
            villageid_column_pos = None
            villagename_column_pos = None
            instanceid_column_pos = None
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    district_column_pos = find_column_position(line, district_column_name)
                    villageid_column_pos = find_column_position(line, villageid_column_name)
                    villagename_column_pos = find_column_position(line, villagename_column_name)
                    instanceid_column_pos = find_column_position(line, 'instanceid')
                    continue
                instanceid = line[instanceid_column_pos]
                if instanceid == '':
                    continue
                if instanceid in instanceid_set:
                    # print(f'Duplicate {instanceid} inside Upa Sarpanch Survey_WIDE.csv')
                    continue
                instanceid_set[instanceid] = {
                    'district': line[district_column_pos].split('.0')[0],
                    'villagename': line[villagename_column_pos],
                    'villageid': line[villageid_column_pos].split('.0')[0]
                }

    file_suffixes = ['1', '2', '2_bis', '3', '4']
    for file_suffix in file_suffixes:
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files/Upa_Sarpanch_Survey_{file_suffix}.csv'
        if not os.path.isfile(file_path):
            raise Exception(f'{file_path} is not valid ')
        try:
            with open(file_path, 'r', encoding='utf-8') as original:
                lines = csv.reader(original, delimiter=',')
                skip_first = True
                district_column_pos = None
                villageid_column_pos = None
                villagename_column_pos = None
                instanceid_column_pos = None
                for line in lines:
                    if skip_first is True:
                        skip_first = False
                        district_column_pos = find_column_position(line, district_column_name)
                        villageid_column_pos = find_column_position(line, villageid_column_name)
                        villagename_column_pos = find_column_position(line, villagename_column_name)
                        instanceid_column_pos = find_column_position(line, 'instanceid')
                        continue
                    villageid = line[villageid_column_pos]
                    if villageid:
                        continue
                    instanceid = line[instanceid_column_pos]
                    district = line[district_column_pos]
                    villagename = line[villagename_column_pos]

                    result = instanceid_set.get(instanceid)
                    if result is None:
                        print(f'Could not find a village id in Upa_Sarpanch_Survey_{file_suffix}.csv for {instanceid} {district} {villagename}')
                    else:
                        expected_result = {
                            'district': district,
                            'villagename': villagename,
                            'villageid': result['villageid']
                        }
                        if result != expected_result:
                            print(f'Found a village id for {instanceid} in Upa_Sarpanch_Survey_{file_suffix}.csv but {json.dumps(result)} vs {json.dumps(expected_result)}')
        except Exception as exp:
            raise Exception(f'Failed for Upa_Sarpanch_Survey_{file_suffix}.csv : {str(exp)}')


if __name__ == '__main__':
    main(sys.argv)
