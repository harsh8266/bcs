import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("files.csv")
x = df['x'].values
y = df['y'].values

# Fit a 2nd degree polynomial using polyfit
degree = 2
coeffs = np.polyfit(x, y, degree)
poly_eq = np.poly1d(coeffs)

# Predicted values
y_pred = poly_eq(x)

# Plotting
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Noisy Data')
plt.plot(x, y_pred, color='blue', label='Fitted Polynomial Curve')
plt.title('Polynomial Curve Fitting using polyfit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
