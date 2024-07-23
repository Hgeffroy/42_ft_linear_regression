from lib.Datasets import BidimensionalData
import matplotlib.pyplot as plt
import csv


class LinearModel:
    """
        Linear model that can be trained from a bidimensional dataset
    """

    def __init__(self, file):
        self.__intersect = 0
        self.__slope = 0
        self.__file = file
        try:
            with open(file, newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                data.__next__()
                tmp = data.__next__()
                self.__intersect = float(tmp[0])
                self.__slope = float(tmp[1])
        except FileNotFoundError:
            self.__store_model(file)

    def __compute_next_step(self, data_x, data_y, learning_rate):
        error_sum_intersect = 0
        error_sum_slope = 0
        for x, y in zip(data_x, data_y):
            error_sum_intersect += y - self.evaluate(x)
            error_sum_slope += (y - self.evaluate(x)) * x

        step_intersect = learning_rate * error_sum_intersect / len(data_x)
        step_slope = learning_rate * error_sum_slope / len(data_x)

        return step_intersect, step_slope

    def __store_model(self, file):
        with open(file, 'w', newline='') as csvfile:
            file = csv.writer(csvfile, delimiter=',')
            file.writerow(['intersect'] + ['slope'])
            file.writerow([self.__intersect, self.__slope])

    def train(self, dataset: BidimensionalData, learning_rate: float,
              max_iterations: int = 10000, normalized: bool = True):

        if normalized is True:
            data_x, data_y = dataset.get_normalized_data()
        else:
            data_x, data_y = dataset.get_data()

        for i in range(max_iterations):
            error_sum_intersect = 0
            error_sum_slope = 0
            for x, y in zip(data_x, data_y):
                error_sum_intersect += y - self.evaluate(x)
                error_sum_slope += (y - self.evaluate(x)) * x

            step_intersect, step_slope = (
                self.__compute_next_step(data_x, data_y, learning_rate))

            if abs(step_intersect) < 0.0000001 and abs(step_slope) < 0.0000001:
                break

            self.__intersect += step_intersect
            self.__slope += step_slope

        if normalized is True:
            norm_x, norm_y = dataset.get_normalization_values()
            self.__intersect *= norm_y
            self.__slope *= norm_y / norm_x

        self.__store_model(self.__file)

    def evaluate(self, to_evaluate: float):
        return self.__intersect + self.__slope * to_evaluate

    def r_squared(self, dataset: BidimensionalData):
        data_x, data_y = dataset.get_data()

        mean = sum(data_y) / len(data_y)
        residual_sum = sum([(y - self.evaluate(x))**2
                            for x, y in zip(data_x, data_y)])
        total_sum = sum([(y - mean)**2 for y in data_y])

        return 1 - (residual_sum / total_sum)

    def show(self, dataset: BidimensionalData, title: str = '',
             x_label: str = '', y_label: str = ''):
        x, y1 = dataset.get_data()
        y2 = [self.evaluate(x) for x in x]
        plt.scatter(x, y1, color='blue')
        plt.plot(x, y2, color='red')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def print(self):
        print(f'intersect: {self.__intersect}')
        print(f'slope: {self.__slope}')

    def reset(self):
        self.__intersect = 0
        self.__slope = 0
        self.__store_model(self.__file)
