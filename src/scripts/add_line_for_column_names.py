#!/usr/bin/python3
import sys
from os import listdir
from os.path import join, isfile


def main(argv):
    new_path = 'C:/Data_PoloFr/scrap-python-indian-gov/new_specific_states_with_columns/'
    path = 'C:/Data_PoloFr/scrap-python-indian-gov/new_specific_states'
    for f in listdir(path):
        file_path = join(path, f)
        if not isfile(file_path) or not f.startswith('results_'):
            continue
        new_file_path = join(new_path, f)
        with open(file_path, 'r') as original:
            data = original.read()
            with open(new_file_path, 'w') as modified:
                modified.write('A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S\n' + data)


if __name__ == '__main__':
    main(sys.argv)
