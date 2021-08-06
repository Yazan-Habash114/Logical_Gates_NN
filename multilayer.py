from Perceptron_M import Perceptron
import random

In_data = [(0, 0), (0, 1), (1, 0), (1, 1)]
out_data = [0, 1, 1, 0]
delta_w_out = []
delta_w_hidden = []
delta_threshould = []
input_layer = [Perceptron(), Perceptron()]

for i in input_layer:
    i.make_input()

hidden_layer = [Perceptron(), Perceptron()]
for h in hidden_layer:
    h.add_input()
    h.weight[0], h.weight[1] = random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)
    print("weights are {0}".format(h.weight),h.threshold)

outp = Perceptron()
outp.add_input()
outp.weight[0], outp.weight[1] = random.uniform(-1.2, 1.2), random.uniform(-1.2, 1.2)
print("output layer are ", outp.weight, outp.threshold)
ep = int(input("Enter # of epochs\n"))
alpha = float(input("Enter learning rate\n"))

for epoch in range(ep):
    print("Epoch # {0}".format(epoch + 1))
    for i in range(len(In_data)):
        delta_w_out.clear()
        delta_w_hidden.clear()
        delta_threshould.clear()
        input_layer[0].In[0], input_layer[1].In[0] = In_data[i]
        for ip in input_layer:
            ip.get_output()
        for h in hidden_layer:
            h.In[0], h.In[1] = input_layer[0].out, input_layer[1].out
            h.get_output()
        outp.In[0], outp.In[1] = hidden_layer[0].out, hidden_layer[1].out
        outp.get_output()
        e = out_data[i] - outp.out
        print("actual output is {0} desired output {1} error {2}".format(outp.out, out_data[i], e))
        #########################################################################
        g5 = outp.out * (1 - outp.out) * e
        for w in range(len(outp.weight)):
            delta_w_out.append(alpha * outp.In[w] * g5)
        delta_threshould.append(alpha * outp.wIn * g5)
        for h in range(len(hidden_layer)):
            gr = hidden_layer[h].out * (1 - hidden_layer[h].out) * (g5 * outp.weight[h])
            for j in range(len(hidden_layer[h].weight)):
                delta_w_hidden.append(alpha * hidden_layer[h].In[j] * gr)
            delta_threshould.append(alpha * hidden_layer[h].wIn * gr)
        for w in range(len(outp.weight)):
            outp.weight[w] += delta_w_out[w]
        index = 0
        for h in hidden_layer:
            for j in range(len(h.weight)):
                h.weight[j] += delta_w_hidden[index]
                index += 1
        outp.threshold += delta_threshould[0]
        hidden_layer[0].threshold += delta_threshould[1]
        hidden_layer[1].threshold += delta_threshould[2]