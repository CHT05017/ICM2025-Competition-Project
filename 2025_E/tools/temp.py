import numpy as np
import matplotlib.pyplot as plt

# 定义常量
NDL = 274.79
CM = 3.7
C = 0

# 定义 T' 的范围
T_prime = np.linspace(0, 10, 400)

# 计算 RM
RM = 0.70 * T_prime + C

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制 CM 和 RM
plt.plot(T_prime, [CM] * len(T_prime), label='CM = 3.7', color='blue')
plt.plot(T_prime, RM, label="RM = 0.70 * T' + C", color='red')

# 填充 RM < CM 的部分
plt.fill_between(T_prime, RM, CM, where=(RM < CM), interpolate=True, color='lightgreen', alpha=0.3, label='RM < CM')

# 填充 RM > CM 的部分
plt.fill_between(T_prime, RM, CM, where=(RM > CM), interpolate=True, color='lightblue', alpha=0.3, label='RM > CM')

# 添加标签和图例
plt.xlabel("T'")
plt.ylabel("values")
plt.legend()

# 显示图形
plt.show()