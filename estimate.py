import sys
from utils import get_thetas


def estimate(mileage):

    try:
        theta0, theta1 = get_thetas('assets/variables.csv')
    except (FileNotFoundError, PermissionError):
        print('variables.csv not found')
        sys.exit(2)
    except ValueError:
        print('variables.csv is corrupted')
        sys.exit(1)

    estimated_value = theta0 + theta1 * mileage
    return estimated_value

