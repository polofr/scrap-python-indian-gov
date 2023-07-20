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
    file_path = PROJECT_ROOT / 'results_wide/results_MAHARASHTRA_2020.csv'
    if not os.path.isfile(file_path):
        return
    all_villages = {
        'PUNE': {},
        'SOLAPUR': {}
    }
    with open(file_path, 'r') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                continue
            district = line[3].strip().upper()
            if district != 'PUNE' and district != 'SOLAPUR':
                continue
            block_name = line[5].strip().upper()
            panchayat_name = line[7].strip().upper()
            panchayat_id = line[9].strip().upper()
            block_villages = all_villages[district].get(block_name)
            if block_villages is None:
                all_villages[district][block_name] = []
            all_villages[district][block_name].append({
                'name': panchayat_name,
                'id': panchayat_id,
                'line': line
            })

    file_path = PROJECT_ROOT / 'villages/sarpanch.csv'
    if not os.path.isfile(file_path):
        return

    result_lines = []
    with open(file_path, 'r') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                continue
            village_id = line[0]
            village_name = line[5].upper().replace('GRAMPANCHAYAT', '').replace('GRAMPANCHAYT', '')\
                .replace(', AKKALKOT', '').replace('(BHOINJE)', '').replace('SAPATNE(BHO)', 'SAPATNE (BHOSE)')\
                .replace('GRAMPANCHYAT', '').replace('GRAMPANACHAYAT', '').replace('GRAM PANCHAYT', '')\
                .replace('GRAMAPANCHAYAT', '').strip()

            block_name = line[7]
            if block_name == '1':
                block_name = 'MADHA'
            elif block_name == '2':
                block_name = 'AKKALKOT'
            elif block_name == '3':
                block_name = 'SOUTH SOLAPUR'
            elif block_name == '4':
                block_name = 'PANDHARPUR'
            elif block_name == '5':
                block_name = 'MOHOL'
            elif block_name == '6':
                block_name = 'BHOR'
            elif block_name == '7':
                block_name = 'BARAMATI'
            elif block_name == '8':
                block_name = 'DAUND'
            elif block_name == '9':
                block_name = 'MULSHI'
            elif block_name == '10':
                block_name = 'KHED'
            else:
                raise Exception(f'No block_name found for {line}')

            district_name = line[6]
            if district_name == '1':
                district_name = 'SOLAPUR'
                if block_name not in ['MADHA', 'AKKALKOT', 'SOUTH SOLAPUR', 'PANDHARPUR', 'MOHOL']:
                    print(f'District and block mistmatch for {line}')
                    continue
            elif district_name == '2':
                district_name = 'PUNE'
                if block_name not in ['BHOR', 'BARAMATI', 'DAUND', 'MULSHI', 'KHED']:
                    print(f'District and block mistmatch for {line}')
                    continue
            else:
                print(f'No district found for {line}')
                continue

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
                for idx, cmp_result in enumerate(cmp_results[0:4]):
                    print('{:>2} {}'.format(cmp_result['score'], cmp_result['match']))
                print()
                selected_row = read_user_input() - 1
                if selected_row < 4:
                    line = cmp_results[selected_row]['line']
                elif selected_row == 4:
                    line = []
            new_line = [village_id, village_name] + line
            result_lines.append(new_line)

        new_file_path = PROJECT_ROOT / 'villages/merge_sarpanch.csv'
        CsvWriter.write(new_file_path, result_lines)


if __name__ == '__main__':
    main(sys.argv)
