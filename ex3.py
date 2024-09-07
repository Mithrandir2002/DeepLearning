import matplotlib.pyplot as plt
import numpy as np
import csv

salary = []
workingTime = []
loanDecision = []
with open("Data_Exercise2.xlsx - Sheet1.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    for row in reader:
        salary.append(float(row[0]))
        workingTime.append(float(row[1]))
        loanDecision.append(float(row[2]))

refuseSalary = []
refuseWorkingTime = []
loanSalary = []
loanWorkingTime = []

for i in range(len(loanDecision)):
    if loanDecision[i] == 0:
        refuseSalary.append(salary[i])
        refuseWorkingTime.append(workingTime[i])
    else:
        loanSalary.append(salary[i])
        loanWorkingTime.append(workingTime[i])

plt.scatter(refuseSalary, refuseWorkingTime, c="blue")
plt.scatter(loanSalary, loanWorkingTime, c="red")
plt.title("Loan Decision base on Salary and Working Time")
plt.xlabel("Salary")
plt.ylabel("Working Time")

x = np.linspace(0, 10)
y = -0.25 * x + 2.25
plt.plot(x, y)

plt.show()