import sys
from get_files_infos import get_thetas

if len(sys.argv) != 2:
    print('Usage: python3 estimate.py [Theta0] [Theta1] [Mileage]')
    print('You can use the trained model to get Theta0 and Theta1')
    sys.exit(1)

try:
    Theta0, Theta1 = get_thetas('./assets/variables.tmp')
except (FileNotFoundError, PermissionError):
    print('variables.tmp not found')
    sys.exit(2)
except ValueError:
    print('variables.tmp is corrupted')
    sys.exit(1)

try:
    Mileage = int(sys.argv[1])
except ValueError:
    print('Mileage must be an integer')
    sys.exit(2)

estimatedValue = Theta0 + Theta1 * Mileage
print('The estimated value of the car is', estimatedValue)
