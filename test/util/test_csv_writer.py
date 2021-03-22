import unittest

from src.util.csv_writer import CsvWriter


class TestCsvWriter(unittest.TestCase):

    def test_csv(self):
        file_path = 'test.csv'
        lines = [
            ['a', 'b', 'c'],
            ['1', '3', '2'],
            ['a', 'b', 'c'],
            [1, 2, 3]
        ]
        CsvWriter.write(file_path, lines)


if __name__ == '__main__':
    unittest.main()
