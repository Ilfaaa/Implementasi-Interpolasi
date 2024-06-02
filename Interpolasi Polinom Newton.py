import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Fungsi untuk menghitung polinom Newton
def newton_interpolation(x, y, x_new):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:,0] = y
        for j in range(1, n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
        return coef[0, :]  # return first row
    
    def newton_poly(coef, x, x_new):
        n = len(coef)
        poly = coef[n-1]
        for k in range(1, n):
            poly = coef[n-k-1] + (x_new - x[n-k-1]) * poly
        return poly
    
    coef = divided_diff(x, y)
    return newton_poly(coef, x, x_new)

# Menghitung nilai interpolasi untuk rentang x baru
x_new = np.linspace(5, 40, 100)
y_new = newton_interpolation(x, y, x_new)

# Plot hasil interpolasi
plt.plot(x, y, 'o', label='Data Asli')
plt.plot(x_new, y_new, '-', label='Interpolasi Newton')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Polinom Newton')
plt.show()
