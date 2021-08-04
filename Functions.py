import math


def step(x):
    if x >= 0:
        return 1
    else:
        return 0


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return (2 / (1 + math.exp(-x)))-1


def ReLU(x):
    if x >= 0:
        return x
    else:
        return 0


def linear(x):
    return x
