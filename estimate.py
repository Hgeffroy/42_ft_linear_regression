import sys
from utils import get_thetas


def estimate(mileage):

    try:
        theta0, theta1 = get_thetas('./assets/variables.tmp')
    except (FileNotFoundError, PermissionError):
        print('variables.tmp not found')
        sys.exit(2)
    except ValueError:
        print('variables.tmp is corrupted')
        sys.exit(1)

    estimated_value = theta0 + theta1 * mileage
    return estimated_value
