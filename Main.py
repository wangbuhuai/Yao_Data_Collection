# Created by Dayu Wang (dwang@stchas.edu) on 2026-02-15

# Last updated by Dayu Wang (dwang@stchas.edu) on 2026-02-15


from csv import DictReader
from typing import TextIO
from File_IO.Input_File import open_input_file, verify_input_file


def main():
    # Open the input file.
    filename: str = open_input_file()
    if len(filename.strip()) == 0:
        print('[Program Exited] No Input File Selected')
        return
    input_file: TextIO = open(
        encoding='utf-8',
        errors='ignore',
        file=filename,
        mode='r'
    )
    csv_reader: DictReader = DictReader(input_file, delimiter=',')

    # Test whether the file opened is a valid CEO or firm database file.
    if verify_input_file(csv_reader) is None:
        print('[Program Exited] Invalid Input File Selected')
        return

    print(csv_reader.fieldnames)


if __name__ == '__main__':
    main()