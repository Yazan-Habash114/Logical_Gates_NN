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


def derv_tanh(x):
    return 1 - x ** 2


def derv_sigmoid(x):
    return x * (1 - x)


def derv_linear(x):
    return 1


def derv_ReLU(x):
    return 1 if x >= 0 else 0


def determine_activation_function(name):
    if name == 'step':
        return step
    elif name == 'linear':
        return linear
    elif name == 'sigmoid':
        return sigmoid
    elif name == 'tanh':
        return tanh
    elif name == 'ReLU':
        return ReLU


def my_formatter(num):
    return float('{0:.3f}'.format(num))
