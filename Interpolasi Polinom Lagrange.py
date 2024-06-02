import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung polinom Lagrange
def lagrange_interpolation(x, y, x_new):
    def L(k, x):
        l = [(x - x[j])/(x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(l, axis=0)
    
    return sum(y[k] * L(k, x_new) for k in range(len(x)))

# Menghitung nilai interpolasi untuk rentang x baru
x_new = np.linspace(5, 40, 100)
y_new = lagrange_interpolation(x, y, x_new)

# Plot hasil interpolasi
plt.plot(x, y, 'o', label='Data Asli')
plt.plot(x_new, y_new, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Polinom Lagrange')
plt.show()
