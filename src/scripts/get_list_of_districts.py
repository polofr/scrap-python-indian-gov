#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from src.util.orchestrator import Main


def print_usage(executable_name, error_msg=None):
    print('Extract data from indian government website')
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
    Main.run()


if __name__ == '__main__':
    main(sys.argv)
