from Perceptron import Perceptron
from functions import *
import random


mean_square_error = 0.0


def calculate(weights_hidden_ml, weights_out_ml, thresholds_ml, x1, x2, func_h, func_out):
    func_h = determine_activation_function(func_h)
    func_out = determine_activation_function(func_out)
    y1 = my_formatter(func_h(x1 * weights_hidden_ml[0] + x2 * weights_hidden_ml[1] - thresholds_ml[0]))
    y2 = my_formatter(func_h(x1 * weights_hidden_ml[2] + x2 * weights_hidden_ml[3] - thresholds_ml[1]))
    y5 = my_formatter(func_out(y1 * weights_out_ml[0] + y2 * weights_out_ml[1] - thresholds_ml[2]))
    return y5


def learn(in_data, out_data, ep, alpha, func_hidden, func_output):
    # Determine the function and its derivative to be used
    func_hidden = determine_activation_function(func_hidden)
    func_output = determine_activation_function(func_output)
    derv_hidden = match_derivative(func_hidden)
    derv_output = match_derivative(func_output)

    delta_w_out = []
    delta_w_hidden = []
    delta_threshold = []
    input_layer = [Perceptron(), Perceptron()]

    for perceptron in input_layer:
        perceptron.make_input()

    hidden_layer = [Perceptron(), Perceptron()]
    for h in hidden_layer:
        h.add_input()
        h.weight[0], h.weight[1] = random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)
        h.activation_fun = func_hidden  # Select function for hidden
        print("weights are {0}".format(h.weight), h.threshold)

    out_perceptron = Perceptron()
    out_perceptron.add_input()
    out_perceptron.activation_fun = func_output  # Select function for output
    print("output layer are ", out_perceptron.weight, out_perceptron.threshold)

    for epoch in range(ep):
        print("Epoch # {0}".format(epoch + 1))
        errors = list()
        for perceptron in range(len(in_data)):  # Get data tuple by tuple
            # Feed forward NN process
            delta_w_out.clear()
            delta_w_hidden.clear()
            delta_threshold.clear()
            input_layer[0].In[0], input_layer[1].In[0] = in_data[perceptron]

            for ip in input_layer:  # Calculate output for each input perceptron
                ip.get_output()

            for h in hidden_layer:  # For each perceptron in the hidden layer
                h.In[0], h.In[1] = input_layer[0].out, input_layer[1].out
                h.get_output()  # Calculate output for each hidden perceptron

            # Transfer output from hidden to ouput
            out_perceptron.In[0], out_perceptron.In[1] = hidden_layer[0].out, hidden_layer[1].out
            out_perceptron.get_output()

            # Calculate Error
            e = my_formatter(out_data[perceptron] - out_perceptron.out)
            errors.append(my_formatter(e ** 2))
            print("actual output is {0} desired output {1} error {2}".format(out_perceptron.out,
                                                                             out_data[perceptron], e))

            # **********************************************************************************
            # **********************************************************************************

            # Back-Propagation process
            gradient_output = derv_output(out_perceptron.out) * e
            for w in range(len(out_perceptron.weight)):  # Delta_w for each weight
                delta_w_out.append(alpha * out_perceptron.In[w] * gradient_output)

            delta_threshold.append(alpha * out_perceptron.wIn * gradient_output)  # Delta_threshold

            # Calculate delta_w for each weight in the hidden layer
            for h in range(len(hidden_layer)):
                gradient_hidden = derv_hidden(hidden_layer[h].out) * (gradient_output * out_perceptron.weight[h])
                for j in range(len(hidden_layer[h].weight)):
                    delta_w_hidden.append(alpha * hidden_layer[h].In[j] * gradient_hidden)
                delta_threshold.append(alpha * hidden_layer[h].wIn * gradient_hidden)

            # Update weights before going to next iteration
            for w in range(len(out_perceptron.weight)):
                out_perceptron.weight[w] += delta_w_out[w]

            index = 0
            for h in hidden_layer:
                for j in range(len(h.weight)):
                    h.weight[j] += delta_w_hidden[index]
                    index += 1

            # Update thresholds
            out_perceptron.threshold += delta_threshold[0]
            hidden_layer[0].threshold += delta_threshold[1]
            hidden_layer[1].threshold += delta_threshold[2]

        global mean_square_error
        for error in errors:
            mean_square_error += error
        mean_square_error /= 4
        mean_square_error = my_formatter(mean_square_error)
        print(f'errors = {errors}')
        errors.clear()
        print(f'mean_square_error = {mean_square_error}, epoch = {epoch + 1}')
        if mean_square_error <= 0.0001:
            break

    # Save weights and thresholds to return them
    weights_hidden = list()
    weights_out = list()
    thresholds = list()
    for h in hidden_layer:
        for j in range(len(h.weight)):
            weights_hidden.append(h.weight[j])

    for w in range(len(out_perceptron.weight)):
        weights_out.append(out_perceptron.weight[w])

    thresholds.append(hidden_layer[0].threshold)
    thresholds.append(hidden_layer[1].threshold)
    thresholds.append(out_perceptron.threshold)

    return weights_hidden, weights_out, thresholds
