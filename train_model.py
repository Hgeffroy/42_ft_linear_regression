import sys
from utils import get_data, update_thetas
from estimate import estimate

Mileages = []
Prices = []
try:
    Mileages, Prices = get_data('./assets/data.csv')
except (FileNotFoundError, PermissionError):
    sys.exit(2)

learningRate0 = 0.1
learningRate1 = learningRate0 / (max(Mileages))**2
Step0 = 1
Step1 = 1
Nb_iter = 0

while (abs(Step0) > 0.001 or abs(Step1) > 0.001) and Nb_iter < 10000:
    ErrorSum0 = 0
    ErrorSum1 = 0

    for mileage, price in zip(Mileages, Prices):
        ErrorSum0 += price - estimate(mileage)
        ErrorSum1 += (price - estimate(mileage)) * mileage

    Step0 = ErrorSum0 * learningRate0 / len(Mileages)
    Step1 = ErrorSum1 * learningRate1 / len(Mileages)

    try:
        update_thetas('assets/variables.csv', Step0, Step1)
    except (ValueError, IndexError, FileNotFoundError, PermissionError):
        sys.exit(2)

    Nb_iter += 1

print(Nb_iter)
