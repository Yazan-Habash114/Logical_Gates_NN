from Perceptron_M import Perceptron
import random

In_data = [(0, 0), (0, 1), (1, 0), (1, 1)]
out_data = [0, 1, 1, 0]
delta_w_out = []
delta_w_hidden = []
delta_threshold = []
input_layer = [Perceptron(), Perceptron()]

for input_perceptron in input_layer:
    input_perceptron.make_input()

hidden_layer = [Perceptron(), Perceptron()]
for hidden in hidden_layer:
    hidden.add_input()
    hidden.weight[0], hidden.weight[1] = random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)
    print("weights are {0}".format(hidden.weight), hidden.threshold)

out_perceptron = Perceptron()
out_perceptron.add_input()
out_perceptron.weight[0], out_perceptron.weight[1] = random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)
print("output layer are ", out_perceptron.weight, out_perceptron.threshold)

ep = int(input("Enter # of epochs\n"))
alpha = float(input("Enter learning rate\n"))

for epoch in range(ep):
    print("Epoch # {0}".format(epoch + 1))
    for input_perceptron in range(len(In_data)):
        delta_w_out.clear()
        delta_w_hidden.clear()
        delta_threshold.clear()
        input_layer[0].In[0], input_layer[1].In[0] = In_data[input_perceptron]
        for ip in input_layer:
            ip.get_output()
        for hidden in hidden_layer:
            hidden.In[0], hidden.In[1] = input_layer[0].out, input_layer[1].out
            hidden.get_output()
        out_perceptron.In[0], out_perceptron.In[1] = hidden_layer[0].out, hidden_layer[1].out
        out_perceptron.get_output()
        e = out_data[input_perceptron] - out_perceptron.out
        print("actual output is {0} desired output {1} error {2}".format(out_perceptron.out, out_data[input_perceptron], e))
        #########################################################################
        g5 = out_perceptron.out * (1 - out_perceptron.out) * e
        for w in range(len(out_perceptron.weight)):
            delta_w_out.append(alpha * out_perceptron.In[w] * g5)
        delta_threshold.append(alpha * out_perceptron.wIn * g5)
        for hidden in range(len(hidden_layer)):
            gr = hidden_layer[hidden].out * (1 - hidden_layer[hidden].out) * (g5 * out_perceptron.weight[hidden])
            for j in range(len(hidden_layer[hidden].weight)):
                delta_w_hidden.append(alpha * hidden_layer[hidden].In[j] * gr)
            delta_threshold.append(alpha * hidden_layer[hidden].wIn * gr)
        for w in range(len(out_perceptron.weight)):
            out_perceptron.weight[w] += delta_w_out[w]
        index = 0
        for hidden in hidden_layer:
            for j in range(len(hidden.weight)):
                hidden.weight[j] += delta_w_hidden[index]
                index += 1
        out_perceptron.threshold += delta_threshold[0]
        hidden_layer[0].threshold += delta_threshold[1]
        hidden_layer[1].threshold += delta_threshold[2]