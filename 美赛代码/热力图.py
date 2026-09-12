import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 创建一个10x10的网格，模拟地点风险系数（rho_L）和韧性系数（lambda_R）
risk_factors = np.random.rand(100, 100)  # 假设的地点风险系数（0-1之间的随机值）
resilience_factors = np.random.rand(100, 100)  # 假设的韧性系数（0-1之间的随机值）

# 2. 创建热力图
# 画地点风险系数的热力图
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # 1行2列，绘制第1个子图
sns.heatmap(risk_factors, cmap='hot', annot=False, cbar_kws={'label': 'Risk Coefficient ($\\rho_L$)'})
plt.title("Location Risk Heatmap ($\\rho_L$)")
plt.xlabel("Location Index")
plt.ylabel("Location Index")

# 画韧性系数的热力图
plt.subplot(1, 2, 2)  # 1行2列，绘制第2个子图
sns.heatmap(resilience_factors, cmap='YlGnBu', annot=False, cbar_kws={'label': 'Resilience Coefficient ($\\lambda_R$)'})
plt.title("Resilience Heatmap ($\\lambda_R$)")
plt.xlabel("Location Index")
plt.ylabel("Location Index")

# 显示两个热力图
plt.tight_layout()
plt.show()
