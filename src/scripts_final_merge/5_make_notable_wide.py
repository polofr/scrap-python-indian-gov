#!/usr/bin/python3
import os
import sys

import pandas as pd

from src.config import PROJECT_ROOT


def main(argv):
    file_path = (
        PROJECT_ROOT
        / "src"
        / "scripts_final_merge"
        / "csv_files_merged"
        / "Notable_Survey_.csv"
    )
    if not os.path.isfile(file_path):
        raise Exception(f"{file_path} is not valid")
    df = pd.read_csv(file_path, dtype=str)
    columns = df.columns
    columns = columns.delete(columns.get_loc("villageid"))
    columns = columns.to_list()
    print(columns)

    df["idx"] = df.groupby("villageid").cumcount()
    df = df.pivot_table(
        index="villageid", columns="idx", values=columns, aggfunc="first"
    )
    df = df.sort_index(axis=1, level=1)
    df.columns = [f"{x}_{y}" for x, y in df.columns]
    df = df.reset_index()
    file_path = (
        PROJECT_ROOT
        / "src"
        / "scripts_final_merge"
        / "csv_files_merged"
        / "Notable_Survey_Wide.csv"
    )
    df.to_csv(path_or_buf=file_path, index=False)


if __name__ == "__main__":
    main(sys.argv)
