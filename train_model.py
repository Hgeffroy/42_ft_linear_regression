import sys
from file_management import get_data, update_thetas
from estimate import estimate

learningRate = 0.01

Mileages = []
Prices = []
try:
    Mileages, Prices = get_data('./assets/data.csv')
except (FileNotFoundError, PermissionError):
    print('data.csv not found')
    sys.exit(2)

m = len(Mileages)
ErrorSum0 = 0
ErrorSum1 = 0

for mileage, price in zip(Mileages, Prices):
    ErrorSum0 += price - estimate(mileage)
    # ErrorSum1 += (estimate(mileage) - price) / mileage

update_thetas('assets/variables.tmp',
              ErrorSum0 * learningRate / m,
              ErrorSum1 * learningRate / m)

# Stop when step < 0.001 TODO
