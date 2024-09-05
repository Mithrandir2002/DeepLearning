import matplotlib.pyplot as plt
import numpy as np
import csv


def GradientDescentForTwoVariablesEquation(intercept, slope, listOfX, listOfY, learningRate, count):
    if count == 100:
        newSlope = slope
        newIntercept = intercept
        return [newSlope, newIntercept]
    else:
        print(f'count {count}')
        derivativeWrtSlope = 0
        derivativeWrtIntercept = 0
        for i in range(len(listOfX)):
            derivativeWrtSlope += (slope * listOfX[i] + intercept - listOfY[i]) * listOfX[i]
            # print(f"derivate wrt slope {derivativeWrtSlope}")
            derivativeWrtIntercept += slope * listOfX[i] + intercept - listOfY[i]
            # print(f"derivate wrt intercept {derivativeWrtIntercept}")
        newSlope = slope - 1/len(listOfX) * derivativeWrtSlope * learningRate
        # print(f'newSlope {newSlope}')
        newIntercept = intercept - 1/len(listOfX) * derivativeWrtIntercept * learningRate
        # print(f'newIntercept {newIntercept}')
        count += 1
        return GradientDescentForTwoVariablesEquation(newIntercept, newSlope, listOfX, listOfY, learningRate, count)


Square = []
Price = []

with open('Data_Exercise1.xlsx - Sheet1.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    header = next(lines)
    for row in lines:
        Square.append(float(row[0]))
        Price.append(float(row[1]))

    Result = GradientDescentForTwoVariablesEquation(0, 0, Square, Price, 0.0001, 0)
    print(f"Result: {Result}")

plt.scatter(Square, Price)
plt.xlabel('Square')
plt.ylabel('Price')
plt.title('Scatter Plot of Square vs. Price', fontsize=20)
x = np.linspace(0, 100)
y = Result[0] * x + Result[1]
plt.plot(x, y, color='blue')
plt.show()




