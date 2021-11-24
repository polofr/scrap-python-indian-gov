#!/usr/bin/python3
import csv
import os
import sys


def main(argv):
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Notable Survey_WIDE_Merged.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')

    initial_data = set()

    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For survey, district is q6 =?= {line[20]}')
                print(f'For survey, villageid =?= {line[15]}')
                print(f'For survey, village name is q1 =?= {line[19]}')
                continue
            if line[20] == '3.0' or line[20] == '3':
                if f'{line[15]}|{line[19]}' in initial_data:
                    print(f'Duplicate entry for {line[15]}, {line[19]}')
                initial_data.add(f'{line[15]}|{line[19]}')
    print(f'Found {len(initial_data)} in initial survey for Ahmednagar district')

    new_data = set()
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/ahmednagar/Notable Survey_WIDE.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For survey, district is q6 =?= {line[20]}')
                print(f'For survey, villageid =?= {line[15]}')
                print(f'For survey, village name is q1 =?= {line[19]}')
                continue
            if f'{line[15]}|{line[19]}' in new_data:
                print(f'Duplicate entry for in new {line[15]}, {line[19]}')
            new_data.add(f'{line[15]}|{line[19]}')

    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/ahmednagar/Notable Survey_WIDE (1).csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For survey, district is q6 =?= {line[20]}')
                print(f'For survey, villageid =?= {line[15]}')
                print(f'For survey, village name is q1 =?= {line[19]}')
                continue
            if f'{line[15]}|{line[19]}' in new_data:
                print(f'Duplicate entry for in new {line[15]}, {line[19]}')
            new_data.add(f'{line[15]}|{line[19]}')

    for entry in initial_data:
        if entry not in new_data:
            print(f'{entry} is in initial but not new')

    for entry in new_data:
        if entry not in initial_data:
            print(f'{entry} is in new but not initial')

    print(f'Found {len(new_data)} in new survey for Ahmednagar district')


if __name__ == '__main__':
    main(sys.argv)
