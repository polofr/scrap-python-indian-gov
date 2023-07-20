#!/usr/bin/python3
import os
import sys

import pandas

from src.config import PROJECT_ROOT


def main(argv):
    filenames = [
        "Gram_Sevak_Survey_Merged_20210904",
        "Group_Survey_Merged_20210824",
        "Notable_Survey_20201026",
        "Sarpanch_Survey_Merged_20210824",
        "Upa_Sarpanch_Survey_Merged_20210824",
    ]
    for filename in filenames:
        file_path = PROJECT_ROOT / f"dta_files/{filename}.dta"
        new_file_path = PROJECT_ROOT / f"csv_files/{filename}.csv"
        if not os.path.isfile(file_path):
            print(f"Could not find {file_path}")
            continue
        data = pandas.io.stata.read_stata(file_path)
        data.to_csv(new_file_path)


if __name__ == "__main__":
    main(sys.argv)
