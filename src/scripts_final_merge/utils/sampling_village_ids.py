import os
import csv
import textdistance


class SamplingVillageIds:
    all_villages = {
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
    def prepare():
        SamplingVillageIds.prepare_ahmednagar()
        SamplingVillageIds.prepare_pune()
        SamplingVillageIds.prepare_solapur()

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
