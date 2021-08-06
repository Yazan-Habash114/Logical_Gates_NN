import random
import functions


def my_formatter(num):
    return float('{0:.3f}'.format(num))


class Perceptron:
    def __init__(self):
        self.In = [0]
        self.wIn = -1
        self.weight = [random.random() - 0.5]  # So weight is in (-0.5, 0.5)
        self.threshold = 2 * random.random() - 1  # So weight is in (-1, 1)
        # self.weight = [0.3]
        # self.threshold = 0.2
        self.activation_fun = functions.step
        self.out = 0.0

    def add_input(self):
        self.In.append(0)
        self.weight.append(random.random() - 0.5)  # So weight is in (-0.5, 0.5)
        # self.weight.append(-0.1)
        print(f'Weight is {self.weight}')
        print(f'Threshold = {self.threshold}')

    def make_input(self):
        self.wIn = 0
        self.weight = [1]
        self.threshold = 1
        self.activation_fun = functions.linear
        self.out = 0.0

    def get_output(self):
        big_X = 0.0
        for i in range(len(self.In)):
            big_X += self.In[i] * self.weight[i]
        big_X += self.threshold * self.wIn
        big_X = my_formatter(big_X)
        self.out = my_formatter(self.activation_fun(big_X))
        print(f'big_x = {big_X}, out = {self.out}')