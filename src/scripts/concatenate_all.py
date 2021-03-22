#!/usr/bin/python3
import sys
from os import listdir
from os.path import join, isfile


def main(argv):
    new_path = 'C:/Data/scrap-python-indian-gov/all/'
    new_file_path = join(new_path, 'all.csv')

    path = 'C:/Data/scrap-python-indian-gov/'

    with open(new_file_path, 'w') as modified:
        modified.write('A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S\n')
        for f in listdir(path):
            file_path = join(path, f)
            if not isfile(file_path) or not f.startswith('results_'):
                continue
            with open(file_path, 'r') as original:
                data = original.read()
                modified.write(data)


if __name__ == '__main__':
    main(sys.argv)
