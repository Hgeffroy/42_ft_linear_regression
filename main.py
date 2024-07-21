from estimate import estimate

try:
    Mileage = int(input('What is the mileage of your car ?\n'))
    print('The estimated value of your car is '
          + str(estimate(Mileage)) + ' euros')
except ValueError:
    print('Please enter a number')
