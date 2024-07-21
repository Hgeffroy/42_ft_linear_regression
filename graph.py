import matplotlib.pyplot as plt
from utils import get_data, get_thetas, normalize_data

x, y1 = get_data('./assets/data.csv')
# x = normalize_data(x)
# y1 = normalize_data(y1)
Theta0, Theta1 = get_thetas('./assets/variables.tmp')
y2 = []

for mileage in x:
    y2.append(Theta0 + mileage * Theta1)

plt.scatter(x, y1, color='blue')
plt.plot(x, y2, color='red')

plt.title('Price of cars given their mileage')
plt.xlabel('mileage(km)')
plt.ylabel('price(euro)')
plt.legend()

plt.show()
