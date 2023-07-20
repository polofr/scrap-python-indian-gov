#!/usr/bin/python3
import os
import sys
import csv
import textdistance

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from src.config import PROJECT_ROOT
from src.util.csv_writer import CsvWriter


def read_user_input():
    value = input('Please enter 1 to 5\n')
    try:
        value = int(value)
        if value < 1 or value > 5:
            raise
    except:
        value = input('Please enter 1 to 5\n')
        value = int(value)
        if value < 1 or value > 5:
            raise Exception('Incorrect input')
    return value


def main(argv):
    file_path = PROJECT_ROOT / 'results_wide/results_HARYANA_2020.csv'
    if not os.path.isfile(file_path):
        return
    all_villages = {}
    chosen_matches = {}
    with open(file_path, 'r') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                continue
            district = line[3].strip().upper()
            block_name = line[5].strip().upper().replace(' (PART)', '')
            panchayat_name = line[7].strip().upper()
            panchayat_id = line[9].strip().upper()
            if all_villages.get(district) is None:
                all_villages[district] = {}
            block_villages = all_villages[district].get(block_name)
            if block_villages is None:
                all_villages[district][block_name] = []
            all_villages[district][block_name].append({
                'name': panchayat_name,
                'id': panchayat_id,
                'line': line
            })

    file_path = PROJECT_ROOT / 'villages/Haryana_new_incomplete.csv'
    if not os.path.isfile(file_path):
        return

    result_lines = []
    with open(file_path, 'r') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = 1
        for line in lines:
            if skip_first > 0:
                skip_first -= 1
                continue
            village_id = line[0]
            village_name = line[1].upper().strip()
            district_name = line[12].upper().strip()
            block_name = line[13].replace(' 1', '-I').replace(' 2', '-II').replace('Bhattu', 'Bhattu Kalan')\
                .replace('Ballabhgarh', 'Ballabgarh').replace('Nissing', 'Nissing At Chirao')\
                .replace('Meham', 'Maham').replace('Lakhan', 'Lakhan Majra') \
                .replace('GHARAUNDA (PART)', 'GHARAUNDA')\
                .replace('Block Saha', 'Saha').replace('Block Naraingarh', 'Naraingarh')\
                .replace('Block Shahzadpur', 'Shahzadpur').replace('Block Barara', 'Barara')\
                .upper().strip().replace('BLOCK ', f'{district_name}-')
            if all_villages.get(district_name) is None:
                raise Exception(f'Invalid district {district_name} for {line}')
            if all_villages[district_name].get(block_name) is None:
                raise Exception(f'Invalid {block_name} for {line}')

            cmp_results = []
            for village in all_villages[district_name][block_name]:
                cmp_results.append({
                    'score': textdistance.damerau_levenshtein(village_name, village['name']),
                    'match': village['name'],
                    'id': village['id'],
                    'line': village['line']
                })
            cmp_results.sort(key=lambda v: v['score'])
            print(f'{district_name} - {block_name} - {village_name} vs {cmp_results[0]["match"]} = {cmp_results[0]["score"]}')

            line = cmp_results[0]['line']
            if cmp_results[0]['score'] > 10:
                selected_row = chosen_matches.get(f'{district_name} - {block_name} - {village_name}')
                if selected_row is None:
                    for idx, cmp_result in enumerate(cmp_results[0:4]):
                        print('{:>2} {}'.format(cmp_result['score'], cmp_result['match']))
                    print()
                    selected_row = read_user_input() - 1
                    chosen_matches[f'{district_name} - {block_name} - {village_name}'] = selected_row
                if selected_row < 4:
                    line = cmp_results[selected_row]['line']
                elif selected_row == 4:
                    line = []
            new_line = [village_id, village_name] + line
            result_lines.append(new_line)

        new_file_path = PROJECT_ROOT / 'villages/merge_sarpanch_haryana.csv'
        CsvWriter.write(new_file_path, result_lines)


if __name__ == '__main__':
    main(sys.argv)
