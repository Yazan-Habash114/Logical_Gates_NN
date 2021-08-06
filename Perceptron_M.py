import random
import functions


class Perceptron:
    def __init__(self):
        self.In = [0]
        self.wIn = -1
        self.weight = [random.random()-0.5]
        self.threshold = 2.4*random.random()-1.2
        self.activation_fun = functions.sigmoid
        self.out = 0.0

    def add_input(self):
        self.In.append(0)
        self.weight.append(random.random()-0.5)

    def get_output(self):
        big_X = 0.0
        for i in range(len(self.In)):
            big_X += self.In[i]*self.weight[i]
        big_X += self.threshold*self.wIn
        self.out = self.activation_fun(big_X)

    def make_input(self):
        self.wIn = 0
        self.weight = [1]
        self.threshold = 1
        self.activation_fun = functions.linear
        self.out = 0.0