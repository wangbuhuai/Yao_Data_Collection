# Created by Dayu Wang (dwang@stchas.edu) on 2026-02-15

# Last updated by Dayu Wang (dwang@stchas.edu) on 2026-02-15


DEFAULT_INPUT_FILE_DIRECTORY: str = '../../Raw_Databases'

# Columns in CEO database (no order requirement, case-insensitive)
CEO_DATABASE_COLUMNS = [
    'DirectorName',
    'CompanyName',
    'BrdPosition',
    'RoleName',
    'FulltextDescription',
    'NED',
    'DirectorID',
    'CompanyID',
    'DateStartRole',
    'DateEndRole',
    'HOCountryName',
    'Sector',
    'OrgType',
    'ISIN'
]

# Columns in firm database (no order requirement, case-insensitive)
FIRM_DATABASE_COLUMNS = [
    'PERMNO',
    'date',
    'EXCHCD',
    'SICCD',
    'NCUSIP',
    'TICKER',
    'COMNAM',
    'PERMCO',
    'HEXCD',
    'CUSIP'
]