from Perceptron import Perceptron
In_data = [(0, 0), (0, 1), (1, 0), (1, 1)]
out_data = [0, 0, 0, 1]
p = Perceptron()
p.add_input()
ep = int(input("Enter # of epochs\n"))
alpha = float(input("Enter learning rate\n"))
for epoch in range(ep):
    print("Epoch # {0}".format(epoch + 1))
    for i in range(4):
        p.In[0], p.In[1] = In_data[i]
        print("{0}    {1}".format( p.In[0], p.In[1]))
        p.get_outout()
        e = out_data[i] - p.out
        print("d is {0}".format(p.out))
        for j in range(len(p.weight)):
            p.weight[j] += alpha*p.In[j]*e


