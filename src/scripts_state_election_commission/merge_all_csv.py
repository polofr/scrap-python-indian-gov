#!/usr/bin/python3
import sys
from os import listdir
from os.path import join, isfile


def main(argv):
    path = 'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_state_election_commission/results'
    new_path = 'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_state_election_commission/merged_results.csv'
    with open(new_path, 'a', encoding='utf8') as merged_file:
        for f in listdir(path):
            file_path = join(path, f)
            if not isfile(file_path):
                continue
            with open(file_path, 'r', encoding='utf8') as to_append:
                data = to_append.read()
                merged_file.write(data)


if __name__ == '__main__':
    main(sys.argv)
