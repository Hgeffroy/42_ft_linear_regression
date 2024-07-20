import sys
from get_files_infos import get_data

learningRate = 1

Mileages = []
Prices = []
try:
    Mileages, Prices = get_data('./assets/data.csv')
except (FileNotFoundError, PermissionError):
    print('data.csv not found')
    sys.exit(2)
