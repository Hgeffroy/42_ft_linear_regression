import sys

if len(sys.argv) != 2:
    print('Usage: python3 estimate.py [Theta0] [Theta1] [Mileage]')
    print('You can use the trained model to get Theta0 and Theta1')
    sys.exit(1)

try:
    file = open('./variables.tmp', 'r')
except (FileNotFoundError, PermissionError):
    print('Theta0 and Theta1 file not found')
    sys.exit(3)

for each in file:
    if 'Theta0=' in each:
        try:
            Theta0 = float(each.split('=')[1])
        except ValueError:
            print('variables.tmp is corrupted')
            sys.exit(1)
    elif 'Theta1=' in each:
        try:
            Theta1 = float(each.split('=')[1])
        except ValueError:
            print('variables.tmp is corrupted')
            sys.exit(1)

if 'Theta0' not in locals() or 'Theta1' not in locals():
    print('One of the variables is missing in variables.tmp')
    sys.exit(2)

try:
    Mileage = int(sys.argv[1])
except ValueError:
    print('Mileage must be an integer')
    sys.exit(2)

estimatedValue = Theta0 + Theta1 * Mileage
print('The estimated value of the car is', estimatedValue)
