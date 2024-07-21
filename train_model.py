import sys
from utils import (get_data, update_thetas, normalize_data,
                   denormalize_thetas)
from estimate import estimate

learningRate = 0.02
Mileages = []
Prices = []
try:
    Mileages, Prices = get_data('./assets/data.csv')
    Mileages = normalize_data(Mileages)
    Prices = normalize_data(Prices)
except (FileNotFoundError, PermissionError):
    sys.exit(2)

Step0 = 1
Step1 = 1
Nb_iter = 0

while (abs(Step0) > 0.0001 or abs(Step1) > 0.0001) and Nb_iter < 10000:
    ErrorSum0 = 0
    ErrorSum1 = 0

    for mileage, price in zip(Mileages, Prices):
        ErrorSum0 += price - estimate(mileage)
        ErrorSum1 += (price - estimate(mileage)) * mileage

    Step0 = ErrorSum0 * learningRate / len(Mileages)
    Step1 = ErrorSum1 * learningRate / len(Mileages)

    try:
        update_thetas('assets/variables.csv', Step0, Step1)
    except (ValueError, IndexError, FileNotFoundError, PermissionError):
        sys.exit(2)

    Nb_iter += 1

try:
    denormalize_thetas('./assets/data.csv', 'assets/variables.csv')
except (ValueError, IndexError, FileNotFoundError, PermissionError):
    sys.exit(2)
