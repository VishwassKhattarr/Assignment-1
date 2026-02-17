# ==============================
# Assignment-1 Solution
# ==============================

import numpy as np
import pandas as pd



data = pd.read_csv("data.csv", encoding="latin1")



print(data.columns)

# Assume column name is "NO2"
x = data["no2"].dropna().values




r = 102303170

# compute parameters
ar = 0.05 * (r % 7)
br = 0.3 * ((r % 5) + 1)

print("a_r =", ar)
print("b_r =", br)

# transformation
z = x + ar * np.sin(br * x)



# mean (mu)
mu = np.mean(z)

# variance
variance = np.var(z)

# lambda estimation (Gaussian relation)
lam = 1 / (2 * variance)

c = np.sqrt(lam / np.pi)



print("\n===== FINAL PARAMETERS =====")
print("mu =", mu)
print("lambda =", lam)
print("c =", c)
