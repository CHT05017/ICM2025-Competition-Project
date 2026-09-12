import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 给定的时间轴和数据
years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
values = np.array([431, 382, 456, 391, 390, 373, 433, 365, 416, 492, 481])

# 进行线性回归
slope, intercept, r_value, p_value, std_err = stats.linregress(years[:len(values)], values)

# 定义预测函数
def predict(year):
    return slope * year + intercept

# 预测 2011 年到 2020 年的值
predicted_years = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
predicted_values = predict(predicted_years)

# 打印预测结果
for year, value in zip(predicted_years, predicted_values):
    print(f"Predicted value for {year}: {value}")

# 生成预测数据
predicted_values_all = predict(years)

# 绘制数据点和拟合直线
plt.scatter(years[:len(values)], values, label='Data Points')
plt.plot(years, predicted_values_all, color='red', label=f'Fit Line: y = {slope:.4f}x + {intercept:.4f}')
plt.xlabel('Year')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()