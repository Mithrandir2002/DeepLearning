import matplotlib.pyplot as plt
import numpy as np


def findMinimumValue(x, learningRate, list):
    if -0.0001 <= 2 * x <= 0.0001:
        return
    else:
        list.append(x)
        x -= 2 * x * learningRate
        findMinimumValue(x, learningRate, list)


x = np.linspace(-2, 2)
y = x * x
list = []
list2 = []

findMinimumValue(-2, 0.01, list)
for element in list:
    list2.append(element * element)

plt.scatter(list, list2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Minimum value of f(x) = x^2 using gradient descent algorithm")

plt.plot(x, y, color='red')
plt.show()