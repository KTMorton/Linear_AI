import math,random


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

class Neuron:

    def __init__(self, weights, bias):
        self.weights = list(weights)
        self.bias = bias
        self.activateValue = 0

    def activate(self, input):
        output = 0
        for idx, element in enumerate(self.weights):
            output += (input[idx] * element)
        output = output + self.bias
        print(output)
        if output > 0:
            self.activateValue = 1
        else:
            self.activateValue = 0

    def getActivateValue(self):
        return self.activateValue


# input1 = [random.randint(0, 5) for i in range(10)]
#
# weights1 = [random.randint(-9, 9) for i in range(10)]
# weights1 = [i/10 for i in weights1]
# bias1 = 1
# print(input1)
# print(weights1)

y_intercept = -3
slopeOfLine = 2
weights1 = [-slopeOfLine, 1]
bias1 = -y_intercept
input1 = [0,0]

neuron1 = Neuron(weights1, bias1)
neuron1.activate(input1)

if neuron1.getActivateValue() == 1:
    print("point is above the line")
else:
    print("point is below the line")








