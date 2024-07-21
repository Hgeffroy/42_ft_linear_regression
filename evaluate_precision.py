import sys
from utils import get_data
from estimate import estimate

try:
    Mileages, Prices = get_data('./assets/data.csv')
except (FileNotFoundError, PermissionError):
    print('data.csv not found')
    sys.exit(2)

mean = 0
for price in Prices:
    mean += price
mean /= len(Prices)

residual_sum = 0
for mileage, price in zip(Mileages, Prices):
    residual_sum += (price - estimate(mileage))**2

total_sum = 0
for price in Prices:
    total_sum += (price - mean)**2

r_squared = 1 - (residual_sum / total_sum)

print('The r squared is ' + str(r_squared))
