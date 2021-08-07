from Perceptron import Perceptron
from functions import *


def calculate(w1, x1, w2, x2, threshold, func):
    test_perceptron = Perceptron()
    test_perceptron.add_input()
    test_perceptron.threshold = threshold
    test_perceptron.In[0] = x1
    test_perceptron.In[1] = x2
    test_perceptron.weight[0] = w1
    test_perceptron.weight[1] = w2
    if func == 'step':
        test_perceptron.activation_fun = step
    elif func == 'linear':
        test_perceptron.activation_fun = linear
    elif func == 'sigmoid':
        test_perceptron.activation_fun = sigmoid
    elif func == 'tanh':
        test_perceptron.activation_fun = tanh
    elif func == 'step':
        test_perceptron.activation_fun = step
    print('\n\nTesting Process')
    test_perceptron.get_output()
    return test_perceptron.out


def learn(in_data, out_data, ep, alpha, func):
    p = Perceptron()
    p.add_input()
    if func == 'step':
        p.activation_fun = step
    elif func == 'linear':
        p.activation_fun = linear
    elif func == 'sigmoid':
        p.activation_fun = sigmoid
    elif func == 'tanh':
        p.activation_fun = tanh
    elif func == 'step':
        p.activation_fun = step

    for epoch in range(ep):
        print(f'Epoch # {epoch + 1}')

        errors = list()
        for i in range(4):
            p.In[0], p.In[1] = in_data[i]
            print(f'{p.In[0]}    {p.In[1]}')
            p.get_output()
            e = my_formatter(out_data[i] - p.out)
            errors.append(my_formatter(e ** 2))
            print(f'a is {p.out}, error = {e}')

            for j in range(len(p.weight)):
                tmp = p.weight[j]
                p.weight[j] += alpha * p.In[j] * e
                p.weight[j] = my_formatter(p.weight[j])
                p.threshold += alpha * p.wIn * e
                p.threshold = my_formatter(p.threshold)
                print(f'Weight is updated by, {my_formatter(p.weight[j]-tmp)}, so weight[{j}] = {p.weight[j]}')
                print(f'New threshold = {p.threshold}')

        mean_square_error = 0.0
        for error in errors:
            mean_square_error += error
        mean_square_error /= 4
        mean_square_error = my_formatter(mean_square_error)
        print(f'errors = {errors}')
        errors.clear()
        print(f'mean_square_error = {mean_square_error}, epoch = {epoch + 1}')
        if mean_square_error <= 0.0001:
            break
        print(f'Threshold = {p.threshold}\n')

    return p.weight[0], p.weight[1], p.threshold
