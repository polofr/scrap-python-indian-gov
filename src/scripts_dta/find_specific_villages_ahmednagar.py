#!/usr/bin/python3
import csv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from src.util.csv_writer import CsvWriter


def correct_village(village_id):
    if '-' in village_id:
        # print('initially ' + village_id)
        village_i = village_id.split('-')
        village_id = '2' + village_i[1].lstrip('0') + village_i[2][2:]
        # print('finally ' + village_id)
    if len(village_id) == 3:
        # print('initially ' + village_id)
        village_id = village_id[0:2] + '0' + village_id[2]
        # print('finally ' + village_id)
    return village_id


def find_position(survey):
    if survey == 'sarpanch':
        position = 0
    elif survey == 'upa-sarpanch':
        position = 1
    elif survey == 'gram-sevak':
        position = 2
    elif survey == 'group':
        position = 3
    elif survey == 'notable':
        position = 4
    else:
        raise Exception(f'Invalid input for survey: {survey}')
    return position


def set_village(village_set, village_id, survey):
    village_id = correct_village(village_id)
    position = find_position(survey)
    entry = village_set.get(village_id)
    if entry is None:
        village_set[village_id] = [0, 0, 0, 0, 0]
    village_set[village_id][position] += 1


def set_village_name(village_name_set, village_id, survey, new_value):
    village_id = correct_village(village_id)
    position = find_position(survey)
    entry = village_name_set.get(village_id)
    if entry is None:
        village_name_set[village_id] = ['', '', '', '', '']
    # if village_name_set[village_id][position] != '' and village_name_set[village_id][position] != new_value:
    #     print(f'For {village_id} {survey} {village_name_set[village_id][position]} vs {new_value}')
    village_name_set[village_id][position] = new_value


def set_gran_sevac_gender(village_set, village_id, sex):
    village_id = correct_village(village_id)
    if sex == '1':
        actual_sex = 'M'
    elif sex == '2':
        actual_sex = 'F'
    elif sex == '3' or sex == '888' or sex == '999':
        actual_sex = 'Unknown'
    else:
        raise Exception(f'Sex is {sex}')
    village_set[village_id] = actual_sex


def set_reservation_for_ahmednagar(village_set, village_id, caste_reservation, gender_reservation):
    if gender_reservation == '1':
        sex = 'F'
    elif gender_reservation == '0':
        sex = 'M'
    else:
        raise Exception(f'gender_reservation is {caste_reservation}')
    if caste_reservation == '2':
        caste = 'OBC'
    elif caste_reservation == '3':
        caste = 'SC'
    elif caste_reservation == '1':
        caste = 'O'
    else:
        raise Exception(f'caste_reservation is {caste_reservation}')
    village_set[village_id] = [sex, caste]


def main(argv):
    village_set = {}
    village_id_to_names = {}
    village_id_to_gan_sevac_sex = {}
    village_id_to_reservation = {}

    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_Ahmednagar.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                continue
            set_reservation_for_ahmednagar(village_id_to_reservation, line[0], line[1], line[2])

    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Sarpanch_Survey_Merged_20210824.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        selected_villages = []
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For Sarpanch survey, district is q6 =?= {line[22]}')
                print(f'For Sarpanch survey, villageid =?= {line[16]}')
                print(f'For Sarpanch survey, village name is q1 =?= {line[21]}')
                continue
            if line[22] == '3.0' or line[22] == '3':
                selected_villages.append(line)
                set_village(village_set, line[16], 'sarpanch')
                set_village_name(village_id_to_names, line[16], 'sarpanch', line[21])

        print(f'Found {len(selected_villages)} in sarpanch survey for Ahmednagar district')

    print('\n\n')
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Upa_Sarpanch_Survey_Merged_20210824.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        selected_villages = []
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For Upa_Sarpanch, district is q6 =?= {line[22]}')
                print(f'For Upa_Sarpanch survey, villageid =?= {line[16]}')
                print(f'For Upa_Sarpanch survey, village name is q1 =?= {line[21]}')
                continue
            if line[22] == '3.0' or line[22] == '3':
                selected_villages.append(line)
                set_village(village_set, line[16], 'upa-sarpanch')
                set_village_name(village_id_to_names, line[16], 'upa-sarpanch', line[21])
        print(f'Found {len(selected_villages)} in Upa_Sarpanch survey for Ahmednagar district')

    print('\n\n')
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Notable Survey_WIDE_Merged.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        selected_villages = []
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For Notable, assuming district is q6 =?= {line[20]}')
                print(f'For Notable survey, villageid =?= {line[15]}')
                print(f'For Notable survey, village name is q1 =?= {line[19]}')
                continue
            if line[20] == '3.0' or line[20] == '3':
                selected_villages.append(line)
                set_village(village_set, line[15], 'notable')
                set_village_name(village_id_to_names, line[15], 'notable', line[19])
        print(f'Found {len(selected_villages)} in Notable survey for Ahmednagar district')

    print('\n\n')
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Gram_Sevak_Survey_Merged_20210904.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        selected_villages = []
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For Gram_Sevak, assuming district is q6 =?= {line[22]}')
                print(f'For Gram_Sevak survey, villageid =?= {line[16]}')
                print(f'For Gram_Sevak survey, village name is q1 =?= {line[21]}')
                print(f'For Gram_Sevak survey, sex is q15 =?= {line[50]}')
                continue
            if line[22] == '3.0' or line[22] == '3':
                selected_villages.append(line)
                set_village(village_set, line[16], 'gram-sevak')
                set_village_name(village_id_to_names, line[16], 'gram-sevak', line[21])
                set_gran_sevac_gender(village_id_to_gan_sevac_sex, line[16], line[50])
        print(f'Found {len(selected_villages)} in Gram_Sevak survey for Ahmednagar district')

    print('\n\n')
    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/Group_Survey_Merged_20210824.csv'
    if not os.path.isfile(file_path):
        raise Exception(f'Failed to find {file_path}')
    with open(file_path, 'r', encoding='utf-8') as original:
        lines = csv.reader(original, delimiter=',')
        skip_first = True
        selected_villages = []
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f'For Group, assuming district is q7 =?= {line[26]}')
                print(f'For Group survey, villageid =?= {line[16]}')
                print(f'For Group survey, village name is q5 =?= {line[25]}')
                continue
            if line[26] == '3.0' or line[26] == '3':
                selected_villages.append(line)
                set_village(village_set, line[16], 'group')
                set_village_name(village_id_to_names, line[16], 'group', line[25])
        print(f'Found {len(selected_villages)} in Group survey for Ahmednagar district')

    print('\n\n')
    print('village ids')
    print(village_set.keys())
    print('village ids end')

    new_csv = []
    new_entry = ['village_id', 'reservation_sex', 'reservation_caste', 'gram_sevak_sex', 'village_name']
    new_csv.append(new_entry)

    villages_with_all = []
    for village_id, surveys in village_set.items():
        if surveys[0] == 0:
            print(f'Missing sarpanch {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[0] != 1:
            print(f'Weird more than one survey for sarpanch {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[1] == 0:
            print(f'Missing upa-sarpanch {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[1] != 1:
            print(f'Weird more than one survey for upa-sarpanch {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[2] == 0:
            print(f'Missing gram-sevak {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[2] != 1:
            print(f'Weird more than one survey for gram-sevak {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[3] == 0:
            print(f'Missing group {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[3] != 1:
            print(f'Weird more than one survey for group {village_id} {village_id_to_names[village_id]}')
            continue
        if surveys[4] < 4:
            print(f'Missing only {surveys[4]} notable {village_id} {village_id_to_names[village_id]}')
            continue
        villages_with_all.append(village_id)
        if village_id_to_reservation.get(village_id) is None:
            print(f'Missing reservation information {village_id} {village_id_to_names[village_id]}')
            continue
        new_entry = [village_id, village_id_to_reservation[village_id][0], village_id_to_reservation[village_id][1], village_id_to_gan_sevac_sex[village_id], village_id_to_names[village_id][0]]
        new_csv.append(new_entry)

    print(f'{len(villages_with_all)} villages with all surveys')
    print(villages_with_all)
    print('villages with all surveys end')

    new_file_path = 'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/results/result_ahmednagar.csv'
    CsvWriter.write(new_file_path, new_csv)


if __name__ == '__main__':
    main(sys.argv)
