#!/usr/bin/python3
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
from src.scripts_state_election_commission.js_executor import JsExecutor


def print_usage(executable_name, error_msg=None):
    print('Extract data from State Election Commission uttar pradesh website')
    print(f'Usage: {executable_name}')
    print()
    if error_msg is not None:
        print(f'Error: {error_msg}')
    sys.exit(1)


def main(argv):
    browser = JsExecutor.get_browser_on_page()
    JsExecutor.submit_form(browser)
    print('done')


if __name__ == '__main__':
    main(sys.argv)
