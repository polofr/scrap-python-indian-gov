#!/usr/bin/python3
import os
import re

import pandas as pd

from src.config import PROJECT_ROOT
from src.scripts_final_merge.utils.columns import COLUMNS


def turn_into_old_format(expected_file_path, file_path, new_file_path):
    if not os.path.isfile(expected_file_path):
        raise Exception(f"{expected_file_path} is not valid")
    data_frame = pd.read_csv(expected_file_path, dtype=str)
    expected_columns = list(data_frame.columns)
    print(
        f'\nExpecting {len(expected_columns)} columns as per {expected_file_path.split("/")[-1]}'
    )
    print(expected_columns)
    print()

    if not os.path.isfile(file_path):
        raise Exception(f"{file_path} is not valid")
    data_frame = pd.read_csv(file_path, dtype=str)

    data_frame = data_frame.drop("audit_URL", axis=1)
    data_frame = data_frame.drop("GPS", axis=1)
    data_frame = data_frame.drop("__version__", axis=1)
    data_frame = data_frame.drop("_version_", axis=1)
    data_frame = data_frame.drop("_version__001", axis=1)
    data_frame = data_frame.drop("background-audio_URL", axis=1)
    if "_version__002" in data_frame.columns:
        data_frame = data_frame.drop("_version__002", axis=1)
    data_frame = data_frame.drop("_validation_status", axis=1)
    data_frame = data_frame.drop("_notes", axis=1)
    data_frame = data_frame.drop("_status", axis=1)
    data_frame = data_frame.drop("_submitted_by", axis=1)
    data_frame = data_frame.drop("_tags", axis=1)

    for old_column in data_frame.columns:
        matches = re.match(r"^Note.+$", old_column)
        if matches:
            data_frame = data_frame.drop(old_column, axis=1)
            continue
        new_column = COLUMNS.get(old_column)
        if new_column:
            if new_column in data_frame.columns:
                print(f"column {new_column} already exists")
            data_frame = data_frame.rename({old_column: new_column}, axis=1)
            continue
        matches = re.match(r"^Q[_0-9]+/[0-9]+$", old_column)
        if matches:
            new_column = old_column.replace("/", "_")
            if new_column in data_frame.columns:
                print(f"column {new_column} already exists 2")
                continue  # TODO
            data_frame = data_frame.rename({old_column: new_column}, axis=1)
            continue

    data_frame["formdef_version"] = ""

    data_frame = data_frame.reindex(columns=expected_columns)

    current_columns = [c for c in data_frame.columns]
    print(f'Currently {len(current_columns)} columns in {file_path.split("/")[-1]}')
    print(current_columns)

    print("columns that should be deleted")
    for column in data_frame.columns:
        if column not in expected_columns:
            print(f"df = df.drop('{column}', axis=1)")
    print("columns that should be added")
    for column in expected_columns:
        if column not in data_frame.columns:
            print(f"df['{column}'] = ''")

    if expected_columns != current_columns:
        raise Exception("Columns are not matching")

    data_frame.to_csv(path_or_buf=new_file_path, index=False)


def main():
    expected_file_path = PROJECT_ROOT / "csv_files/ahmednagar/Notable Survey_WIDE.csv"
    file_path = (
        PROJECT_ROOT
        / "csv_files/amravati/Notable_Survey_Amravati_-_all_versions_-_False_-_2022-07-29-05.csv"
    )
    new_file_path = (
        PROJECT_ROOT / "src/scripts_final_merge/csv_files/Notable_Survey_5.csv"
    )
    turn_into_old_format(expected_file_path, file_path, new_file_path)

    file_path = (
        PROJECT_ROOT
        / "csv_files/aurangabad/Notable_Survey_-_all_versions_-_False_-_2022-04-01-05.csv"
    )
    new_file_path = (
        PROJECT_ROOT / "src/scripts_final_merge/csv_files/Notable_Survey_6.csv"
    )
    turn_into_old_format(expected_file_path, file_path, new_file_path)


if __name__ == "__main__":
    main()
