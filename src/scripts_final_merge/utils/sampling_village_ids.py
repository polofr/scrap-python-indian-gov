import os
import csv
import textdistance


class SamplingVillageIds:
    village_id_to_reservation = {}
    all_villages = {
        '5': [],  # 'AMRAVATI'
        '4': [],  # 'AURANGABAD'
        '3': [],  # 'AHMEDNAGAR'
        '2': [],  # 'PUNE'
        '1': []   # 'SOLAPUR'
    }

    @staticmethod
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

    @staticmethod
    def prepare_reservation():
        SamplingVillageIds.prepare_reservation_for_ahmednagar()
        SamplingVillageIds.prepare_reservation_for_pune()
        SamplingVillageIds.prepare_reservation_for_solapur()
        SamplingVillageIds.prepare_reservation_for_aurangabad()
        SamplingVillageIds.prepare_reservation_for_amravati()

    @staticmethod
    def prepare_reservation_for_amravati():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_Amravati.csv'
        if not os.path.isfile(file_path):
            raise Exception(f'Failed to find {file_path}')
        with open(file_path, 'r', encoding='utf-8') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                gender_reservation = line[3]
                caste_reservation = line[2]
                village_id = line[0].strip()
                print(f'village_id: {int(village_id)}')
                if gender_reservation == 'F':
                    sex = 'F'
                elif gender_reservation == 'OPEN':
                    sex = 'M'
                else:
                    raise Exception(f'gender_reservation is {gender_reservation} for {line}')
                if caste_reservation == 'OBC':
                    caste = 'OBC'
                elif caste_reservation == 'SC':
                    caste = 'SC'
                elif caste_reservation == 'GEN':
                    caste = 'O'
                else:
                    raise Exception(f'caste_reservation is {caste_reservation} for {line}')
                SamplingVillageIds.village_id_to_reservation[village_id] = [sex, caste]

    @staticmethod
    def prepare_reservation_for_aurangabad():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_AURANGABAD.csv'
        if not os.path.isfile(file_path):
            raise Exception(f'Failed to find {file_path}')
        with open(file_path, 'r', encoding='utf-8') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                gender_reservation = line[3].strip()
                caste_reservation = line[2].strip()
                village_id = line[0].strip()
                print(f'village_id: {int(village_id)}')
                if gender_reservation == 'F' or gender_reservation == 'Female':
                    sex = 'F'
                elif gender_reservation == 'Open' or gender_reservation == 'OPEN':
                    sex = 'M'
                else:
                    raise Exception(f'gender_reservation is {gender_reservation} for {line}')
                if caste_reservation == 'OBC':
                    caste = 'OBC'
                elif caste_reservation == 'SC':
                    caste = 'SC'
                elif caste_reservation == 'General' or caste_reservation == 'GENRAL' or caste_reservation == 'GENERAL':
                    caste = 'O'
                else:
                    raise Exception(f'caste_reservation is {caste_reservation} for {line}')
                SamplingVillageIds.village_id_to_reservation[village_id] = [sex, caste]

    @staticmethod
    def prepare_reservation_for_ahmednagar():
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
                from src.scripts_dta.find_specific_villages_ahmednagar import set_reservation_for_ahmednagar
                set_reservation_for_ahmednagar(SamplingVillageIds.village_id_to_reservation, line[0], line[1], line[2])

    @staticmethod
    def prepare_reservation_for_pune():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_PUNE.csv'
        if not os.path.isfile(file_path):
            raise Exception(f'Failed to find {file_path}')
        with open(file_path, 'r', encoding='utf-8') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                from src.scripts_dta.find_specific_villages_pune import set_reservation_for_pune
                set_reservation_for_pune(SamplingVillageIds.village_id_to_reservation, line[1], line[0])

    @staticmethod
    def prepare_reservation_for_solapur():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_Solapur.csv'
        if not os.path.isfile(file_path):
            raise Exception(f'Failed to find {file_path}')
        with open(file_path, 'r', encoding='utf-8') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                from src.scripts_dta.find_specific_villages_pune import set_reservation_for_pune
                set_reservation_for_pune(SamplingVillageIds.village_id_to_reservation, line[1], line[0])

    @staticmethod
    def prepare():
        SamplingVillageIds.prepare_ahmednagar()
        SamplingVillageIds.prepare_pune()
        SamplingVillageIds.prepare_solapur()
        SamplingVillageIds.prepare_aurangabad()
        SamplingVillageIds.prepare_amravati()

    @staticmethod
    def prepare_ahmednagar():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_Ahmednagar.csv'
        if not os.path.isfile(file_path):
            return
        with open(file_path, 'r') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                panchayat_name = line[2].strip().lower()
                panchayat_id = line[0].strip().lower()
                SamplingVillageIds.all_villages['3'].append({
                    'name': panchayat_name,
                    'id': panchayat_id
                })

    @staticmethod
    def prepare_pune():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_PUNE.csv'
        if not os.path.isfile(file_path):
            return
        with open(file_path, 'r') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                panchayat_name = line[2].strip().lower()
                panchayat_id = line[1].strip().lower()
                SamplingVillageIds.all_villages['2'].append({
                    'name': panchayat_name,
                    'id': panchayat_id
                })

    @staticmethod
    def prepare_solapur():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_Solapur.csv'
        if not os.path.isfile(file_path):
            return
        with open(file_path, 'r') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                panchayat_name = line[3].strip().lower()
                panchayat_id = line[1].strip().lower()
                SamplingVillageIds.all_villages['1'].append({
                    'name': panchayat_name,
                    'id': panchayat_id
                })

    @staticmethod
    def prepare_amravati():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_Amravati.csv'
        if not os.path.isfile(file_path):
            return
        with open(file_path, 'r') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                panchayat_name = line[1].strip().lower()
                panchayat_id = line[0].strip().lower()
                SamplingVillageIds.all_villages['5'].append({
                    'name': panchayat_name,
                    'id': panchayat_id
                })

    @staticmethod
    def prepare_aurangabad():
        file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/csv_files/sampling/Sampling_AURANGABAD.csv'
        if not os.path.isfile(file_path):
            return
        with open(file_path, 'r') as original:
            lines = csv.reader(original, delimiter=',')
            skip_first = True
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    continue
                panchayat_name = line[1].strip().lower()
                panchayat_id = line[0].strip().lower()
                SamplingVillageIds.all_villages['4'].append({
                    'name': panchayat_name,
                    'id': panchayat_id
                })

    @staticmethod
    def get_all_village_ids():
        all_village_ids = []
        for district_with_villages in SamplingVillageIds.all_villages.values():
            for village in district_with_villages:
                all_village_ids.append(village['id'])
        return all_village_ids

    @staticmethod
    def find_best_match_and_take_output(village_name, district):
        cmp_results = SamplingVillageIds.find_best_match(village_name, district)
        chosen_village = SamplingVillageIds.read_user_input() - 1
        if chosen_village == 4:
            return None
        return cmp_results[chosen_village]['id']

    @staticmethod
    def find_best_match(village_name, district):
        if district.lower() == 'solapur':
            district = '1'
        village_name = village_name.replace('Grampanchayat', '').replace('grampanchayat', '')
        cmp_results = []
        for village in SamplingVillageIds.all_villages[district]:
            cmp_results.append({
                'score': textdistance.hamming(village_name, village['name']),
                'match': village['name'],
                'id': village['id']
            })
        cmp_results.sort(key=lambda v: v['score'])
        print(f'current village name : {village_name}. Suggestions :')
        for idx, cmp_result in enumerate(cmp_results[0:4]):
            print('{} {}'.format(cmp_result['id'], cmp_result['match']))
        return cmp_results
