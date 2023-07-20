#!/usr/bin/python3
import os
import sys
import re
import csv

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from src.config.result_count import RESULT_COUNT
from src.util.orchestrator import Main


def print_usage(executable_name, error_msg=None):
    print(f'Usage: {executable_name} 2017 2017-2018 ASSAM')
    print()
    if error_msg is not None:
        print(f'Error: {error_msg}')
    sys.exit(1)


def main(argv):
    financial_year = argv[1]
    financial_year_plan = argv[2]
    state = ' '.join(argv[3:])

    if financial_year is None or financial_year_plan is None or state is None:
        print_usage(argv[0])
    if not financial_year_plan.startswith(financial_year):
        print_usage(argv[0], 'financial_year_plan usually is financial_year-financial_year+1')

    print(f'''Arguments:
        - financial-year: {financial_year}
        - financial-year-plan: {financial_year_plan}
        - state: {state}''')

    Main.financial_year = financial_year
    Main.financial_year_plan = financial_year_plan
    Main.state_name = state

    file_path = f'/Users/paulhenricarton/polofr_repos/scrap-python-indian-gov/results/results_{state}_{financial_year}.csv'
    if not os.path.isfile(file_path):
        return

    with open(file_path, 'r') as original:
        data = original.read()
        budgets = re.findall(r'Total,', data)
        percentage = 100.0 * len(budgets) / RESULT_COUNT[financial_year][state]
        print(f'{percentage}% {len(budgets)} vs {RESULT_COUNT[financial_year][state]}')

    with open(file_path, 'r') as original:
        lines = csv.reader(original, delimiter=',')
        villages = set()
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                continue
            unique_id = f'{line[7].strip()}-{line[8].strip()}-{line[9].strip()}'
            villages.add(unique_id)
        Main.run(villages)


if __name__ == '__main__':
    main(sys.argv)
