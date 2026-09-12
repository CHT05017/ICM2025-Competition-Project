import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 给定的数据
x = np.array([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])
y = np.array([
116,
139,
223,
147,
199,
172,
236,
268,
254,
263,
300,
343,
329,
351,
415,
368,
430,
364,
413,
407,
441,





])

# 进行线性回归
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# 输出拟合出的函数形式
print(f"拟合出的函数形式: y = {slope:.4f}x + {intercept:.4f}")

# 绘制数据点和拟合直线
plt.scatter(x, y, label='Data Points')
plt.plot(x, slope * x + intercept, color='red', label=f'Fit Line: y = {slope:.4f}x + {intercept:.4f}')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.show()