from src.util.csv_writer import CsvWriter


def test_csv():
    file_path = 'test.csv'
    lines = [
        ['a', 'b', 'c'],
        ['1', '3', '2'],
        ['a', 'b', 'c'],
        [1, 2, 3]
    ]
    CsvWriter.write(file_path, lines)
