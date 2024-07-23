from typing import Tuple
import matplotlib.pyplot as plt
import csv


class BidimensionalData:
    """
        Stores a dataset with 2 data types
    """

    def __init__(self, path: str):
        self._dataX: list[float] = []
        self._dataY: list[float] = []
        self._labelX: str
        self._labelY: str
        with open(path, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            labels = data.__next__()
            self._labelX = labels[0]
            self._labelY = labels[1]
            for row in data:
                self._dataX.append(float(row[0]))
                self._dataY.append(float(row[1]))

    def __str__(self):
        return (f'Abscissa datas:\n{self._dataX}\n'
                f'Ordinate datas:\n{self._dataY}')

    def get_data(self) -> Tuple[list[float], list[float]]:
        return self._dataX, self._dataY

    def get_normalized_data(self) -> Tuple[list[float], list[float]]:
        max_x = max(self._dataX)
        max_y = max(self._dataY)
        return ([x / max_x for x in self._dataX],
                [y / max_y for y in self._dataY])

    def get_max_values(self) -> Tuple[float, float]:
        return max(self._dataX), max(self._dataY)

    def show(self, title: str = ''):
        plt.scatter(self._dataX, self._dataY)
        plt.title(title)
        plt.xlabel(self._labelX)
        plt.ylabel(self._labelY)
        plt.show()

