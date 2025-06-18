import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x**2

a = 0
b = 2

N = 100000  

x_random = np.random.uniform(a, b, N)

integral_mc = (b - a) * np.mean(f(x_random))

print(f"Інтеграл методом Монте-Карло: {integral_mc}")

integral_quad, error = spi.quad(f, a, b)
print(f"Інтеграл методом quad: {integral_quad} (похибка {error})")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y)+0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()
