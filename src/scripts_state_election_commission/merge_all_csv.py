#!/usr/bin/python3
import sys
from os import listdir
from os.path import join, isfile


def main(argv):
    new_csv_lines = []
    path = 'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_state_election_commission/results'
    for f in listdir(path):
        file_path = join(path, f)
        if not isfile(file_path):
            continue
        district_number = f.split('.')[0]
        district_number = district_number.lstrip('0')
        with open(file_path, 'r', encoding='utf8') as to_append:
            lines = to_append.readlines()
            is_first = True
            for line in lines:
                if is_first is True:
                    is_first = False
                    continue
                new_csv_lines.append(f'{district_number},{line}')
    column_names = 'district,ब्लॉक,ग्राम पंचायत,पद का आरक्षण,उम्मीदवार,पिता/पति,प्रत्याशी का आरक्षण,शैक्षिक योग्यता,लिंग,मोबाइल नं०,प्राप्त वैध मत,प्राप्त मत %,मतदान %,परिणाम'
    new_path = 'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_state_election_commission/merged_results.csv'
    with open(new_path, 'w', encoding='utf8') as result_file:
        result_file.writelines([column_names])
        result_file.writelines(new_csv_lines)


if __name__ == '__main__':
    main(sys.argv)
