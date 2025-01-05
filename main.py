#!/usr/bin/env python3

from lib.Datasets import BidimensionalData
from lib.Models import LinearModel
import argparse


def valid_option(opt):
    valid_values = ['evaluate', 'train', 'reset', 'show', 'compare']
    if opt in valid_values:
        return opt
    else:
        raise argparse.ArgumentTypeError(f'{opt} is not a valid option')


def evaluate(model: LinearModel):
    to_evaluate = float(input('What is the mileage of your car ?\n'))
    print(f'Your car is worth about {model.evaluate(to_evaluate)} euros')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('option', type=valid_option,
                        help='[evaluate] [train] [reset]')
    parser.add_argument('-s', '--showdata', action='store_true',
                        help='Show raw datas in a graph')
    parser.add_argument('-S', '--showmodel', action='store_true',
                        help='Show model in a graph with the raw data')
    parser.add_argument('-p', '--precision', action='store_true',
                        help='Print the r squared of the regression')
    parser.add_argument('-d', '--printdata', action='store_true',
                        help='Print the data in the standard output')
    parser.add_argument('-m', '--printmodel', action='store_true',
                        help='Print the model in the standard output')
    args = parser.parse_args()

    data = BidimensionalData('assets/data.csv')
    model = LinearModel('assets/model.csv')

    match args.option:
        case 'compare':
            model.compare_several_training_options(data)
        case 'evaluate':
            evaluate(model)
        case 'train':
            model.train(data)
        case 'reset':
            model.reset()
        case 'show':
            pass

    if args.showdata:
        data.show('Price of the cars given their mileage')
    if args.showmodel:
        model.show(data, 'Price of the cars given their mileage')
    if args.precision:
        print(model.r_squared(data))
    if args.printdata:
        print(data)
    if args.printmodel:
        print(model)



if __name__ == '__main__':
    main()
