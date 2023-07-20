#!/usr/bin/python3
import csv
import json
import os
import sys

from src.config import PROJECT_ROOT
from src.scripts_final_merge.utils.helper import Helper
from src.scripts_final_merge.utils.sampling_village_ids import SamplingVillageIds
from src.util.csv_writer import CsvWriter


def main(argv):

    district_column_name = "q7"
    villageid_column_name = "villageid"
    villagename_column_name = "q5"

    instanceid_set = {}

    files_with_ids = [
        PROJECT_ROOT / "csv_files/ahmednagar/Group Survey_WIDE.csv",
        PROJECT_ROOT / "csv_files/ahmednagar/Group Survey_WIDE (1).csv",
        PROJECT_ROOT / "csv_files/Group_Survey_Merged_20210824.csv",
    ]

    for file_with_ids in files_with_ids:
        if not os.path.isfile(file_with_ids):
            raise Exception(f"{file_with_ids} is not valid")

        with open(file_with_ids, "r", encoding="utf-8") as original:
            lines = csv.reader(original, delimiter=",")
            skip_first = True
            district_column_pos = None
            villageid_column_pos = None
            villagename_column_pos = None
            instanceid_column_pos = None
            for line in lines:
                if skip_first is True:
                    skip_first = False
                    district_column_pos = Helper.find_column_position(
                        line, district_column_name
                    )
                    villageid_column_pos = Helper.find_column_position(
                        line, villageid_column_name
                    )
                    villagename_column_pos = Helper.find_column_position(
                        line, villagename_column_name
                    )
                    instanceid_column_pos = Helper.find_column_position(
                        line, "instanceid"
                    )
                    continue
                instanceid = line[instanceid_column_pos]
                if not instanceid:
                    continue
                if not line[villageid_column_pos]:
                    # print(f'missing village id for {instanceid} inside Group Survey_WIDE.csv')
                    continue
                if instanceid in instanceid_set:
                    # print(f'Duplicate {instanceid} inside Group Survey_WIDE.csv')
                    continue
                instanceid_set[instanceid] = {
                    "district": line[district_column_pos].split(".0")[0],
                    "villagename": line[villagename_column_pos],
                    "villageid": line[villageid_column_pos].split(".0")[0],
                }
    SamplingVillageIds.prepare()
    file_suffixes = ["1", "2", "2_bis", "3", "4"]
    for file_suffix in file_suffixes:
        file_path = (
            PROJECT_ROOT
            / f"src/scripts_final_merge/csv_files/Group_Survey_{file_suffix}.csv"
        )
        if not os.path.isfile(file_path):
            raise Exception(f"{file_path} is not valid")
        try:
            result_lines = []
            with open(file_path, "r", encoding="utf-8") as original:
                lines = csv.reader(original, delimiter=",")
                skip_first = True
                district_column_pos = None
                villageid_column_pos = None
                villagename_column_pos = None
                instanceid_column_pos = None
                for idx, line in enumerate(lines):
                    result_lines.append(line)
                    if skip_first is True:
                        skip_first = False
                        district_column_pos = Helper.find_column_position(
                            line, district_column_name
                        )
                        villageid_column_pos = Helper.find_column_position(
                            line, villageid_column_name
                        )
                        villagename_column_pos = Helper.find_column_position(
                            line, villagename_column_name
                        )
                        instanceid_column_pos = Helper.find_column_position(
                            line, "instanceid"
                        )
                        continue
                    villageid = line[villageid_column_pos]
                    if villageid:
                        continue
                    instanceid = line[instanceid_column_pos]
                    district = line[district_column_pos]
                    villagename = line[villagename_column_pos]

                    result = instanceid_set.get(instanceid)
                    if result is None:
                        print(
                            f"Could not find a village id at line {idx + 1} in Group_Survey_{file_suffix}.csv for {instanceid} {district} {villagename}"
                        )
                        villageid = SamplingVillageIds.find_best_match_and_take_output(
                            villagename, district
                        )
                        if villageid is not None:
                            result_lines[-1][villageid_column_pos] = villageid
                            result_lines[-1][villageid_column_pos + 1] = villageid
                    else:
                        expected_result = {
                            "district": district,
                            "villagename": villagename,
                            "villageid": result["villageid"],
                        }
                        if result != expected_result:
                            print(
                                f"Found a village id for {instanceid} in Group_Survey_{file_suffix}.csv but {json.dumps(result)} vs {json.dumps(expected_result)}"
                            )
                        result_lines[-1][villageid_column_pos] = result["villageid"]
                        result_lines[-1][villageid_column_pos + 1] = result["villageid"]

                CsvWriter.write(
                    file_path.replace("csv_files", "csv_files_corrected"), result_lines
                )
        except Exception as exp:
            raise Exception(f"Failed for Group_Survey_{file_suffix}.csv : {str(exp)}")


if __name__ == "__main__":
    main(sys.argv)
