import matplotlib.pyplot as plt
import csv


class BidimensionalData:
    """
        Stores a dataset with 2 data types
    """

    def __init__(self, file: str):
        self.__dataX = []
        self.__dataY = []
        with open(file, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            data.__next__()

            for row in data:
                self.__dataX.append(int(row[0]))
                self.__dataY.append(int(row[1]))

    def get_data(self):
        return self.__dataX, self.__dataY

    def get_normalized_data(self):
        max_x = max(self.__dataX)
        max_y = max(self.__dataY)
        return ([x / max_x for x in self.__dataX],
                [y / max_y for y in self.__dataY])

    def get_normalization_values(self):
        return max(self.__dataX), max(self.__dataY)

    def print(self):
        print(f'Abscissa datas:\n{self.__dataX}')
        print(f'Ordinate datas:\n{self.__dataY}')

    def show(self, title: str = '',
             x_label: str = '', y_label: str = ''):
        plt.scatter(self.__dataX, self.__dataY)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

