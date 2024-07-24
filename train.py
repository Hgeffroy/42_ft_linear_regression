#!/usr/bin/env python3
from lib.Models import LinearModel
from lib.Datasets import BidimensionalData


def main():
    model = LinearModel('assets/model.csv')
    data = BidimensionalData('assets/data.csv')
    model.train(data, 0.1)


if __name__ == '__main__':
    main()
