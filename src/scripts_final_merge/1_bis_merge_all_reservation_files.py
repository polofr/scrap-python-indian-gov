#!/usr/bin/python3
import sys

from src.scripts_final_merge.utils.sampling_village_ids import SamplingVillageIds
from src.util.csv_writer import CsvWriter


def main(argv):
    SamplingVillageIds.prepare_reservation()
    lines = []
    lines.append(['villageid', 'gender', 'caste'])

    for village_id, values in SamplingVillageIds.village_id_to_reservation.items():
        lines.append([village_id, values[0], values[1]])

    file_path = f'C:/Data_PoloFr/scrap-python-indian-gov/src/scripts_final_merge/csv_files_merged/Sampling.csv'
    CsvWriter.write(file_path, lines)


if __name__ == '__main__':
    main(sys.argv)
