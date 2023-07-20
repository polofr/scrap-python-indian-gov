#!/usr/bin/python3
import csv
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from src.config import PROJECT_ROOT
from src.util.orchestrator import Main


def print_usage(executable_name, error_msg=None):
    print(f"Usage: {executable_name} 2017 2017-2018 ASSAM")
    print()
    if error_msg is not None:
        print(f"Error: {error_msg}")
    sys.exit(1)


def main(argv):
    financial_year = argv[1]
    financial_year_plan = argv[2]
    state = " ".join(argv[3:])

    if financial_year is None or financial_year_plan is None or state is None:
        print_usage(argv[0])
    if not financial_year_plan.startswith(financial_year):
        print_usage(
            argv[0], "financial_year_plan usually is financial_year-financial_year+1"
        )

    print(
        f"""Arguments:
        - financial-year: {financial_year}
        - financial-year-plan: {financial_year_plan}
        - state: {state}"""
    )

    Main.financial_year = financial_year
    Main.financial_year_plan = financial_year_plan
    Main.state_name = state

    file_path = PROJECT_ROOT / "new_results" / f"results_{state}_{financial_year}.csv"
    if not os.path.isfile(file_path):
        return
    with open(file_path, "r") as original:
        lines = csv.reader(original, delimiter=",")
        all_villages = []
        skip_first = True
        previous_village_id = None
        current_budget_id = None
        budget_count = 0
        for line in lines:
            if skip_first is True:
                skip_first = False
                continue
            village_id = " " + line[8]
            budget_id = " " + line[9].strip().lstrip("0")
            if budget_id != current_budget_id:
                current_budget_id = budget_id
                if previous_village_id != village_id:
                    budget_count = 0
                    previous_village_id = village_id
                else:
                    budget_count = budget_count + 1
            line[9] = budget_id
            village = ",".join(line[0:10]) + f", {budget_count}," + ",".join(line[10:])
            all_villages.append(village)

        new_file_path = (
            PROJECT_ROOT / "new_results_2" / f"results_{state}_{financial_year}.csv"
        )
        with open(new_file_path, "w", newline="") as modified:
            modified.write(
                "year, state, state_id, district_panchayat, district_panchayat_id, block_panchayat, block_panchayat_id, village_panchayat, village_panchayat_id, village_panchayat_budget_id, village_panchayat_budget_count, category, sctied, sttied, generaltied, totaltied, scuntied, stuntied, generaluntied, totaluntied\n"
            )
            for village in all_villages:
                modified.write(village + "\n")


if __name__ == "__main__":
    main(sys.argv)
