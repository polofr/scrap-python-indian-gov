#!/usr/bin/python3
import os
import sys
import csv
import json

from src.scripts_final_merge.utils.helper import Helper
from src.scripts_final_merge.utils.sampling_village_ids import SamplingVillageIds


# position sarpanch 0, upa-sarpanch 1 gram-sevak 2 group 3 notable 4
def set_line_length(lines_length, survey_position, village_name, line, origin):
    entry = lines_length[survey_position]
    if entry is None:
        lines_length[survey_position] = {
            'lengths': [],
            'origins': []
        }
    lines_length[survey_position]['lengths'].append(len(line))
    lines_length[survey_position]['origins'].append(f'{village_name} {origin}')


def set_village(village_set, village_id, survey_position, village_name, origin):
    entry = village_set.get(village_id)
    if entry is None:
        village_set[village_id] = {
            'names': [[], [], [], [], []]
        }
    village_set[village_id]['names'][survey_position].append(f'{village_name} {origin}')


def main(argv):
    villageid_column_name = 'villageid'
    lines_length = [None, None, None, None, None]
    village_set = {}
    file_prefixes = ['Sarpanch', 'Upa_Sarpanch', 'Gram_Sevak', 'Group', 'Notable']
    file_suffixes = ['1', '2', '2_bis', '3', '4', '5', '6']
    for survey_position, file_prefix in enumerate(file_prefixes):
        for file_suffix in file_suffixes:
            file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_corrected/{file_prefix}_Survey_{file_suffix}.csv'
            if not os.path.isfile(file_path):
                raise Exception(f'{file_path} is not valid')
            try:
                with open(file_path, 'r', encoding='utf-8') as original:
                    lines = csv.reader(original, delimiter=',')
                    skip_first = True
                    villageid_column_pos = None
                    villagename_column_pos = None
                    for idx, line in enumerate(lines):
                        if skip_first is True:
                            skip_first = False
                            villageid_column_pos = Helper.find_column_position(line, villageid_column_name)
                            if file_prefix == 'Group':
                                villagename_column_name = 'q5'
                            else:
                                villagename_column_name = 'q1'
                            villagename_column_pos = Helper.find_column_position(line, villagename_column_name)
                            continue
                        villageid = line[villageid_column_pos]
                        if not villageid:
                            continue
                        villagename = line[villagename_column_pos]
                        input_origin = f'from line {idx + 1} inside {file_prefix}_Survey_{file_suffix}.csv'
                        set_village(village_set, villageid, survey_position, villagename, input_origin)
                        set_line_length(lines_length, survey_position, villagename, line, input_origin)
            except Exception as exp:
                raise Exception(f'Failed for {file_prefix}_Survey_{file_suffix}.csv : {str(exp)}')

    SamplingVillageIds.prepare()
    all_sampled_village_ids = SamplingVillageIds.get_all_village_ids()

    print(json.dumps(village_set, indent=4, sort_keys=True))
    complete_villages = 0
    for village_id, village in village_set.items():
        if len(village['names'][0]) and len(village['names'][1]) and len(village['names'][2]) and len(village['names'][3]) and len(village['names'][4]) > 3:
            complete_villages += 1
            if village_id not in all_sampled_village_ids:
                print(f'Missing sampling data for {village_id}: {village}')

    print(f'{complete_villages} completed villages')
    for idx, line_length in enumerate(lines_length):
        print(f'For {file_prefixes[idx]}, not all surveys have the same number of columns')
        print(set(line_length['lengths']))



if __name__ == '__main__':
    main(sys.argv)
