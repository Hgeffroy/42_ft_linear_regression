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
        raise ValueError('Theta0 and Theta1 are not defined')

    return theta0, theta1


def get_data(filename):
    mileages = []
    prices = []

    file = open(filename, 'r')

    for each in file:
        try:
            tab = each.split(',')
            mileage = int(tab[0])
            price = int(tab[1])
            mileages.append(mileage)
            prices.append(price)
        except (ValueError, IndexError):
            pass

    return mileages, prices

