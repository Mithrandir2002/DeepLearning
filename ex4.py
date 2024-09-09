import numpy as np
import matplotlib.pyplot as plt

# Predicted probabilities
y_hat = np.linspace(0.01, 0.99, 100)

# True label y_i = 1
y_i = 1

# Loss function
loss = -(y_i * np.log(y_hat) + (1 - y_i) * np.log(1 - y_hat))

# Plotting
plt.plot(y_hat, loss, label=r'Loss when $y_i = 1$')
plt.xlabel(r'$\hat{y}$')
plt.ylabel('Loss')
plt.title('Binary Cross-Entropy Loss Function')
plt.grid(True)
plt.legend()
plt.show()