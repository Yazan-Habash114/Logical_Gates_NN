from Perceptron import Perceptron


def my_formatter(num):
    return float('{0:.3f}'.format(num))


def learn(in_data, out_data):
    p = Perceptron()
    p.add_input()

    ep = int(input('Enter # of epochs\n'))
    alpha = float(input('Enter learning rate\n'))

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

        MSE = 0.0
        for error in errors:
            MSE += error
        MSE /= 4
        MSE = my_formatter(MSE)
        print(f'errors = {errors}')
        errors.clear()
        print(f'MSE = {MSE}, epoch = {epoch + 1}')
        if MSE <= 0.0001:
            break
        print(f'Threshold = {p.threshold}\n')

    return p.weight[0], p.weight[1]


# print(tuple(learn([(0, 0), (0, 1), (1, 0), (1, 1)], [0, 0, 0, 1])))
