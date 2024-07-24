#!/usr/bin/env python3
from main import evaluate
from lib.Models import LinearModel


def main():
    model = LinearModel('assets/model.csv')
    evaluate(model)


if __name__ == '__main__':
    main()
