#!/usr/bin/env python3

from lib.Datasets import BidimensionalData
from lib.Models import LinearModel
import argparse


def args_error():
    print('Usage: ./main.py [-h] option')
    print('Available OPTIONS:\n- evaluate\n- train\n- printdata\n'
          '- printmodel\n- precision\n')


def evaluate(model: LinearModel):
    to_evaluate = float(input('What is the mileage of your car ?\n'))
    print(f'Your car is worth about {model.evaluate(to_evaluate)} euros')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('option')
    args = parser.parse_args()

    data = BidimensionalData('assets/data.csv')
    model = LinearModel('assets/model.csv')

    match args.option:
        case 'evaluate':
            evaluate(model)
        case 'train':
            model.train(data, 0.1)
        case 'showdata':
            data.show(title='Price of cars given their mileage',
                         x_label='Mileage of car(km)',
                         y_label='Price of car(euros)')
        case 'showmodel':
            model.show(data)
        case 'printmodel':
            model.print()
        case 'precision':
            print(model.r_squared(data))
        case 'resetmodel':
            model.reset()
        case _:
            return args_error()


if __name__ == '__main__':
    main()
