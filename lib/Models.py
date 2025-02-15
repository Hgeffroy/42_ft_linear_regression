from lib.Datasets import BidimensionalData
from typing import Tuple
import matplotlib.pyplot as plt
import csv


class LinearModel:
    """
        Linear model that can be trained from a bidimensional dataset
    """

    def __init__(self, file):
        self._intersect: float = 0
        self._slope: float = 0
        self._file: str = file
        try:
            with open(file, newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                data.__next__()
                values = data.__next__()
                self._intersect = float(values[0])
                self._slope = float(values[1])
        except FileNotFoundError:
            self._store_model(file)

    def __str__(self):
        return f'intersect: {self._intersect}\nslope: {self._slope}'

    def _compute_next_step(self, data_x, data_y, learning_rate) -> Tuple[float, float]:
        error_sum_intersect = 0
        error_sum_slope = 0
        for x, y in zip(data_x, data_y):
            error_sum_intersect += y - self.evaluate(x)
            error_sum_slope += (y - self.evaluate(x)) * x

        step_intersect = learning_rate * error_sum_intersect / len(data_x)
        step_slope = learning_rate * error_sum_slope / len(data_x)

        return step_intersect, step_slope

    def _store_model(self, file):
        with open(file, 'w', newline='') as csvfile:
            file = csv.writer(csvfile, delimiter=',')
            file.writerow(['intersect'] + ['slope'])
            file.writerow([self._intersect, self._slope])

    def train(self, dataset: BidimensionalData, learning_rate: float = 0.1,
              max_iterations: int = 10000, normalized: bool = True,
              precision: float = 1e-6):

        if normalized is True:
            data_x, data_y = dataset.get_normalized_data()
        else:
            data_x, data_y = dataset.get_data()

        for i in range(max_iterations):
            step_intersect, step_slope = (
                self._compute_next_step(data_x, data_y, learning_rate))

            if (abs(step_intersect) < precision and
                    abs(step_slope) < precision):
                break

            self._intersect += step_intersect
            self._slope += step_slope

        if normalized is True:
            norm_x, norm_y = dataset.get_max_values()
            self._intersect *= norm_y
            self._slope *= norm_y / norm_x

        self._store_model(self._file)

    def evaluate(self, to_evaluate: float) -> float:
        return self._intersect + self._slope * to_evaluate

    def r_squared(self, dataset: BidimensionalData) -> float:
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

    def reset(self):
        self._intersect = 0
        self._slope = 0
        self._store_model(self._file)

    def compare_several_training_options(self, dataset: BidimensionalData,
                                         precisions_to_test=None,
                                         max_iterations_to_test=None):
        if precisions_to_test is None:
            precisions_to_test = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
        if max_iterations_to_test is None:
            max_iterations_to_test = [10, 100, 1000, 10000, 100000]

        self.reset()
        r_squared_precisions = []
        r_squared_max_iterations = []

        for precision in precisions_to_test:
            self.train(dataset, precision=precision)
            r_squared_precisions.append(self.r_squared(dataset))
            self.reset()

        for max_iteration in max_iterations_to_test:
            self.train(dataset, max_iterations=max_iteration)
            r_squared_max_iterations.append(self.r_squared(dataset))
            self.reset()

        plt.plot(max_iterations_to_test, r_squared_max_iterations)
        plt.title("Precision of regression given number of max iterations")
        plt.xscale('log')
        plt.xlabel("Max iterations")
        plt.ylabel("R-squared")
        plt.show()

        plt.plot(precisions_to_test, r_squared_precisions)
        plt.title("Precision of regression given precision")
        plt.xscale('log')
        plt.xlabel("Max iterations")
        plt.ylabel("R-squared")
        plt.show()


