import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 给定的数据
x = np.array([1,2,3,4,5,6])
y = np.array([0,-0.8,-2,-1.9,-1.7,0
])

# 多项式拟合
degree = 2  # 多项式的阶数
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)

# 生成拟合曲线
x_fit = np.linspace(min(x), max(x), 100)
y_fit_poly = polynomial(x_fit)

# 打印多项式拟合的表达式
poly_expr = " + ".join([f"{coeff:.8f}*x^{degree-i}" for i, coeff in enumerate(coefficients)])
print(f"Polynomial Fit (degree={degree}): y = {poly_expr}")

# 定义指数函数
def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

# 指数函数拟合
popt, pcov = curve_fit(exponential_func, x, y, p0=(1, 0.01, 1), maxfev=200000)

# 生成拟合曲线
y_fit_exp = exponential_func(x_fit, *popt)

# 打印指数函数拟合的表达式
exp_expr = f"{popt[0]:.4f} * exp({popt[1]:.10f} * (x)) + {popt[2]:.4f}"
# print(f"Exponential Fit: y = {exp_expr}")

# 绘制数据点和拟合曲线

plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit_poly, color='red', label=f'Polynomial Fit (degree={degree})')
# plt.plot(x_fit, y_fit_exp, color='green', label='Exponential Fit')
plt.xlabel('Year')
plt.ylabel('Pest. (kg/ha)')
plt.legend()
plt.grid()
plt.show()