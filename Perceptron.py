import random
import Functions


class Perceptron:
    def __init__(self):
        self.In = [0]
        self.wIn = -1
        self.weight = [random.random()]
        self.threshold = random.random()
        self.activation_fun = Functions.ReLU
        self.out = 0.0

    def add_input(self):
        self.In.append(0)
        self.weight.append(random.random())

    def get_outout(self):
        big_X = 0.0
        for i in range(len(self.In)):
            big_X += self.In[i]*self.weight[i]
        big_X += self.threshold*self.wIn
        self.out = self.activation_fun(big_X)
