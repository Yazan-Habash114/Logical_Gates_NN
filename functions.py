import math


def step(x):
    return 1 if x >= 0 else 0


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return (2 / (1 + math.exp(-x))) - 1


def ReLU(x):
    return x if x >= 0 else 0


def linear(x):
    return x


def my_formatter(num):
    return float('{0:.3f}'.format(num))
