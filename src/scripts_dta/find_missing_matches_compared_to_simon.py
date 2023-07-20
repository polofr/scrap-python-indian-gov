#!/usr/bin/python3
import csv
import os
import sys

from src.config import PROJECT_ROOT


def main():
    file_path = PROJECT_ROOT / "csv_files/ahmednagar/Conflicting_report_from_simon.csv"
    if not os.path.isfile(file_path):
        raise Exception(f"Failed to find {file_path}")

    simon_villages = set()

    with open(file_path, "r", encoding="utf-8") as original:
        lines = csv.reader(original, delimiter=",")
        skip_first = True
        for line in lines:
            if skip_first is True:
                skip_first = False
                print(f"For survey, villageid is UNIQUE ID =?= {line[1]}")
                print(f"For survey, all surveys Complete =?= {line[20]}")
                continue
            if line[20] == "1":
                simon_villages.add(line[1])
    print(f"Simon found {len(simon_villages)}")

    alyssa_villages = [
        "3608",
        "3112",
        "3111",
        "3101",
        "3117",
        "3104",
        "3109",
        "3914",
        "3103",
        "3105",
        "3107",
        "3915",
        "3114",
        "3301",
        "3110",
        "3910",
        "3106",
        "3305",
        "3307",
        "3706",
        "3314",
        "3701",
        "3704",
        "3707",
        "3315",
        "3312",
        "3705",
        "3708",
        "3709",
        "3912",
        "3313",
        "3210",
        "3702",
        "3401",
        "3206",
        "3416",
        "3204",
        "3213",
        "3209",
        "3409",
        "3308",
        "3417",
        "3202",
        "3211",
        "3201",
        "3408",
        "3418",
        "3402",
        "3421",
        "3207",
        "3208",
        "3212",
        "3205",
        "3410",
        "3917",
        "3601",
        "3803",
        "3921",
        "3925",
        "3413",
        "3907",
        "3414",
        "3602",
        "3310",
        "3924",
        "3908",
        "3918",
        "3919",
        "3901",
        "3926",
        "3424",
        "3929",
        "3805",
        "3902",
        "3119",
        "3513",
        "3419",
        "3533",
        "3531",
        "3711",
        "3920",
        "3710",
        "3527",
        "3316",
        "3927",
        "3503",
        "3515",
        "3517",
        "3605",
        "3604",
        "3930",
        "3610",
        "3806",
        "3607",
        "3423",
        "3807",
        "3606",
        "3611",
    ]

    alyssa_villages = set(alyssa_villages)
    print(f"Alyssa found {len(alyssa_villages)}")

    for entry in alyssa_villages:
        if entry not in simon_villages:
            print(f"{entry} is in alyssa but not simon")

    for entry in simon_villages:
        if entry not in alyssa_villages:
            print(f"{entry} is in simon but not alyssa")


if __name__ == "__main__":
    main()
