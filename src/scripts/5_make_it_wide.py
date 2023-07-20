#!/usr/bin/python3
import sys
import csv
from os import listdir
from os.path import join, isfile

from src.config import PROJECT_ROOT


def main(argv):
    new_path = PROJECT_ROOT / 'results_wide'
    path = PROJECT_ROOT / 'new_results_2'

    short_categories = ['AdministrativeTechnicalSupport',
                        'AdultEducation',
                        'Agriculture',
                        'AnimalHusbandry',
                        'CulturalActivities',
                        'DrinkingWater',
                        'Education',
                        'FamilyWelfare',
                        'Fisheries',
                        'FuelAndFodder',
                        'GPOfficeInfrastructure',
                        'Health',
                        'HealthSanitation',
                        'Khadi',
                        'LandImprovement',
                        'Libraries',
                        'MaintenanceOfCommunitySystem',
                        'MarketsAndFairs',
                        'MinorForestProduce',
                        'NonConventionalEnergySources',
                        'Others',
                        'PovertyAllevationProgramme',
                        'PublicDistributionSystem',
                        'Roads',
                        'RuralElectrification',
                        'RuralHousing',
                        'Sanitation',
                        'SmallScaleIndustries',
                        'SocialAndFarmForestry',
                        'SocialWelfare',
                        'TechAndVocationalEducation',
                        'TribalWelfare',
                        'WaterConservation',
                        'WelfareOfWeaker',
                        'WomenAndChildDevelopment',
                        'Total']

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
                  'Zotal']

    for f in listdir(path):
        file_path = path / f
        if not isfile(file_path) or not f.startswith('results_'):
            continue
        new_file_path = new_path / f
        with open(file_path, 'r') as original:
            with open(new_file_path, 'w', newline='') as modified:
                modified.write('year, state, state_id, district_panchayat, district_panchayat_id, block_panchayat, block_panchayat_id, village_panchayat, village_panchayat_id, village_panchayat_budget_id, village_panchayat_budget_count')
                for cat in short_categories:
                    modified.write(f', sctied_{cat}, sttied_{cat}, generaltied_{cat}, totaltied_{cat}, scuntied_{cat}, stuntied_{cat}, generaluntied_{cat}, totaluntied_{cat}')
                modified.write('\n')
                csv_writer = csv.writer(modified, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                lines = csv.reader(original, delimiter=',')
                village = {}
                skip_first = True
                for line in lines:
                    if skip_first is True:
                        skip_first = False
                        continue
                    category = line[11].strip()
                    index = categories.index(category)
                    village[index] = line[12:]
                    if category == 'Zotal':
                        entire_row = line[0:11]
                        index = 0
                        while index < len(categories):
                            values = village.get(index)
                            if values:
                                entire_row.extend(values)
                            else:
                                entire_row.extend([' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0', ' 0'])
                            index = index + 1
                        csv_writer.writerow(entire_row)
                        village = {}


if __name__ == '__main__':
    main(sys.argv)
