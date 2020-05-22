import pandas as pd

read_file = pd.read_csv (r'C:\MyFiles\Dhaval\GSM\20200506.PDBTxnDlyTD.csv')
read_file.to_excel (r'C:\MyFiles\Dhaval\GSM\20200506.PDBTxnDlyTD.xlsx', index = None, header=True)