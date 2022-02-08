import numpy as np

x = np.arange(100) ** 2
x_mean = np.mean(x)
print(x_mean)

x_var = np.var(x)
print(x_var)

x_var_self_calc = np.mean((x - x_mean) ** 2)
print(x_var_self_calc)

x_std = np.std(x)
print(x_std)
print(x_var_self_calc ** (1/2))