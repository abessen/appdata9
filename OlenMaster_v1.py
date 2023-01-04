from pathlib import Path  # Python Standard Library
import pandas as pd  # pip install pandas openpyxl


this_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
wb_file_path = this_dir / 'OlenMaster_v1.xlsb'

df = pd.read_excel(
    io=wb_file_path,
    engine='openpyxl',
    sheet_name='eWon',
    skiprows=18,
    usecols='BL:BY',
    nrows=1402,
)
print(df)
