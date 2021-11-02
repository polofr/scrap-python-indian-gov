#!/usr/bin/python3
import sys
from os import listdir
from os.path import join, isfile


def main(argv):
    path = 'C:/Data_PoloFr/scrap-python-indian-gov/'
    new_path = 'C:/Data_PoloFr/scrap-python-indian-gov/results/'
    for f in listdir(path):
        file_path = join(path, f)
        if not isfile(file_path) or not f.startswith('results_'):
            continue
        result_file_path = join(new_path, f)
        with open(file_path, 'r') as to_append:
            with open(result_file_path, 'a') as original:
                data = to_append.read()
                original.write(data)


if __name__ == '__main__':
    main(sys.argv)
