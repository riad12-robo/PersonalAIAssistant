from pybrain.tools.shortcuts import buildNetwork #using buildNetwork we build the network
#param 2,3,1 is nothing but the input layer 2 and hidden layer 3 and the output layer 1
network = buildNetwork(2,3,1)
print(network)