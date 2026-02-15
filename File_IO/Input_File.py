# Created by Dayu Wang (dwang@stchas.edu) on 2026-02-15

# Last updated by Dayu Wang (dwang@stchas.edu) on 2026-02-15


from csv import DictReader
from tkinter import filedialog
from Parameters.Parameters import CEO_DATABASE_COLUMNS, DEFAULT_INPUT_FILE_DIRECTORY, FIRM_DATABASE_COLUMNS


def open_input_file() -> str:
    """ Opens a raw CSV database using tkinter.
        :return: A full pathname to the raw CSV database file
    """
    # Get the default directory for the file dialog.
    file_dir: str = ''
    if DEFAULT_INPUT_FILE_DIRECTORY is not None and len(DEFAULT_INPUT_FILE_DIRECTORY.strip()) > 0:
        file_dir = DEFAULT_INPUT_FILE_DIRECTORY

    # Let the use select a CSV file in a dialog.
    filename: str = filedialog.askopenfilename(
        filetypes=[('CSV Files', '*.csv')],
        initialdir=file_dir,
        title='Open a Raw Database'
    )

    return filename


def verify_input_file(csv_reader: DictReader) -> str|None:
    """ Verifies that the input file is a valid CEO or firm raw database file.
        :param csv_reader: A CSV DictReader to the database file
        :return: 'CEO' or 'firm' or None (invalid input file)
    """
    # Test whether the input file is a valid CEO raw database file.
    mark: bool = True
    for col in csv_reader.fieldnames:
        if col.lower().strip() not in [col.lower() for col in CEO_DATABASE_COLUMNS]:
            mark = False
            break
    if mark:
        return 'CEO'

    # Test whether the input file is a valid firm raw database file.
    mark = True
    for col in csv_reader.fieldnames:
        if col.lower().strip() not in [col.lower() for col in FIRM_DATABASE_COLUMNS]:
            mark = False
            break
    if mark:
        return 'firm'

    return None  # Invalid input file.