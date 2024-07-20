import numpy
import sys
import matplotlib.pyplot as plt
from get_files_infos import get_data

x, y = get_data('./assets/data.csv')

print(x)
print(y)

plt.scatter(x, y, color='blue')

plt.title('Price of cars given their mileage')
plt.xlabel('mileage(km)')
plt.ylabel('price(euro)')
plt.legend()

plt.show()
