#!/usr/bin/python3
import csv
import os
import sys

from src.config import PROJECT_ROOT


def main(argv):
    file_path = PROJECT_ROOT / "csv_files/Sarpanch_Survey_Merged_20210824.csv"
    if not os.path.isfile(file_path):
        raise Exception(f"Failed to find {file_path}")

    initial_data = set()

    with open(file_path, "r", encoding="utf-8") as original:
        lines = csv.reader(original, delimiter=",")
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f"For survey, district is q6 =?= {line[22]}")
                print(f"For survey, villageid =?= {line[16]}")
                print(f"For survey, village name is q1 =?= {line[21]}")
                continue
            if line[22] == "3.0" or line[22] == "3":
                if f"{line[16]}|{line[21]}" in initial_data:
                    print(f"Duplicate entry for {line[16]}, {line[21]}")
                initial_data.add(f"{line[16]}|{line[21]}")
    print(f"Found {len(initial_data)} in initial survey for Ahmednagar district")

    new_data = set()

    file_path = PROJECT_ROOT / "csv_files/ahmednagar/Sarpanch Survey_WIDE (1).csv"
    if not os.path.isfile(file_path):
        raise Exception(f"Failed to find {file_path}")
    with open(file_path, "r", encoding="utf-8") as original:
        lines = csv.reader(original, delimiter=",")
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f"For survey, district is q6 =?= {line[21]}")
                print(f"For survey, villageid =?= {line[15]}")
                print(f"For survey, village name is q1 =?= {line[20]}")
                continue
            if f"{line[15]}|{line[20]}" in new_data:
                print(f"Duplicate entry for in new {line[15]}, {line[20]}")
            new_data.add(f"{line[15]}|{line[20]}")

    file_path = PROJECT_ROOT / "csv_files/ahmednagar/Sarpanch Survey_WIDE.csv"
    if not os.path.isfile(file_path):
        raise Exception(f"Failed to find {file_path}")
    with open(file_path, "r", encoding="utf-8") as original:
        lines = csv.reader(original, delimiter=",")
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f"For survey, district is q6 =?= {line[21]}")
                print(f"For survey, villageid =?= {line[15]}")
                print(f"For survey, village name is q1 =?= {line[20]}")
                continue
            if f"{line[15]}|{line[20]}" in new_data:
                print(f"Duplicate entry for in new {line[15]}, {line[20]}")
            new_data.add(f"{line[15]}|{line[20]}")

    for entry in initial_data:
        if entry not in new_data:
            print(f"{entry} is in initial but not new")

    for entry in new_data:
        if entry not in initial_data:
            print(f"{entry} is in new but not initial")

    print(f"Found {len(new_data)} in new survey for Ahmednagar district")


if __name__ == "__main__":
    main(sys.argv)
