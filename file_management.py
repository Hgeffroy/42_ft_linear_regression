import os


def get_thetas(filename):
    theta0 = None
    theta1 = None

    file = open(filename, 'r')

    for each in file:
        if 'Theta0=' in each:
            theta0 = float(each.split('=')[1])
        elif 'Theta1=' in each:
            theta1 = float(each.split('=')[1])

    if theta0 is None or theta1 is None:
        raise ValueError('Theta0 and/or Theta1 are not defined')

    file.close()
    return theta0, theta1


def get_data(filename):
    mileages = []
    prices = []

    file = open(filename, 'r')
    line = 0

    for each in file:
        try:
            tab = each.split(',')
            mileage = int(tab[0])
            price = int(tab[1])
            mileages.append(mileage)
            prices.append(price)
            line += 1
        except (ValueError, IndexError):
            if line > 0:
                print('Warning: your data looks corrupted')

    file.close()
    return mileages, prices


def update_thetas(filename, step_theta0, step_theta1):
    theta0, theta1 = get_thetas(filename)

    file = open(filename, 'w')
    file.write('Theta0=' + str(theta0 + step_theta0) + '\n')
    file.write('Theta1=' + str(theta1 + step_theta1) + '\n')
    file.close()

