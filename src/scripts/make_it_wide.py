#!/usr/bin/python3
import sys
import csv
from os import listdir
from os.path import join, isfile


def main(argv):
    new_path = 'C:/Data/scrap-python-indian-gov/new_wide/'
    path = 'C:/Data/scrap-python-indian-gov/'

    #  10 + 36 categories * 8
    categories = ['Administrative & Technical Support',
                  'Adult and non-formal education',
                  'Agriculture',
                  'Animal husbandry',
                  'Cultural activities',
                  'Drinking water',
                  'Education',
                  'Family welfare',
                  'Fisheries',
                  'Fuel and fodder',
                  'GP Office Infrastructure',
                  'Health',
                  'Health & Sanitation',
                  'Khadi',
                  'Land improvement',
                  'Libraries',
                  'Maintenance of community system',
                  'Markets and fairs',
                  'Minor forest produce',
                  'Non-conventional energy sources',
                  'Others',
                  'Poverty allevation programme',
                  'Public distribution system',
                  'Roads',
                  'Rural electrification',
                  'Rural housing',
                  'Sanitation',
                  'Small-scale industries',
                  'Social forestry and farm forestry',
                  'Social welfare',
                  'Technical training and vocational education',
                  'Tribal Welfare',
                  'Water Conservation',
                  'Welfare of the weaker sections',
                  'Women and child development',
                  'Total']

    for f in listdir(path):
        file_path = join(path, f)
        if not isfile(file_path) or not f.startswith('results_'):
            continue
        new_file_path = join(new_path, f)
        # new_file_path = 'C:/Data/scrap-python-indian-gov/new_wide/results_ANDAMAN AND NICOBAR ISLANDS_2019.csv'
        # file_path = 'C:/Data/scrap-python-indian-gov/results_ANDAMAN AND NICOBAR ISLANDS_2019.csv'
        with open(file_path, 'r') as original:
            with open(new_file_path, 'w', newline='') as modified:
                modified.write('year, state, state_id, district_panchayat, district_panchayat_id, block_panchayat, block_panchayat_id, village_panchayat, village_panchayat_id, village_panchayat_budget_id')
                index = 1
                while index < len(categories) + 1:
                    modified.write(f', sctied_{index}, sttied_{index}, generaltied_{index}, totaltied_{index}, scuntied_{index}, stuntied_{index}, generaluntied_{index}, totaluntied_{index}')
                    index = index + 1
                modified.write('\n')
                csv_writer = csv.writer(modified, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                lines = csv.reader(original, delimiter=',')
                village = {}
                for line in lines:
                    category = line[10].strip()
                    index = categories.index(category)
                    village[index] = line[11:]
                    if category == 'Total':
                        entire_row = line[0:10]
                        index = 0
                        while index < len(categories):
                            values = village.get(index)
                            if values:
                                entire_row.extend(values)
                            else:
                                entire_row.extend([0, 0, 0, 0, 0, 0, 0, 0])
                            index = index + 1
                        csv_writer.writerow(entire_row)
                        village = {}


if __name__ == '__main__':
    main(sys.argv)
