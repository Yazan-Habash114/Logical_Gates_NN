from Perceptron import Perceptron
from functions import *
import random


def learn(in_data, out_data, ep, alpha, func_output, func_hidden):
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
        h.activation_fun = determine_activation_function(func_hidden)  # Select function for hidden
        print("weights are {0}".format(h.weight), h.threshold)

    out_perceptron = Perceptron()
    out_perceptron.add_input()
    out_perceptron.activation_fun = determine_activation_function(func_output)  # Select function for output
    print("output layer are ", out_perceptron.weight, out_perceptron.threshold)

    for epoch in range(ep):
        print("Epoch # {0}".format(epoch + 1))
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
            e = out_data[perceptron] - out_perceptron.out
            print("actual output is {0} desired output {1} error {2}".format(out_perceptron.out, out_data[perceptron], e))

            # **********************************************************************************
            # Back-Propagation process
            # gradient_output = out_perceptron.out * (1 - out_perceptron.out) * e
            gradient_output = (1 - out_perceptron.out ** 2) * e
            for w in range(len(out_perceptron.weight)):  # Delta_w for each weight
                delta_w_out.append(alpha * out_perceptron.In[w] * gradient_output)

            delta_threshold.append(alpha * out_perceptron.wIn * gradient_output)  # Delta_threshold

            # Calculate delta_w for each weight in the hidden layer
            for h in range(len(hidden_layer)):
                # gradient_hidden = hidden_layer[h].out * (1 - hidden_layer[h].out) * \
                #                   (gradient_output * out_perceptron.weight[h])
                gradient_hidden = (1 - hidden_layer[h].out ** 2) * \
                                  (gradient_output * out_perceptron.weight[h])
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


learn([(0, 0), (0, 1), (1, 0), (1, 1)], [1, 0, 0, 1], 5000, 0.14, 'tanh', 'tanh')
