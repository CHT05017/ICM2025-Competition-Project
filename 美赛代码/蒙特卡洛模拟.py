import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from matplotlib.colors import Normalize

# 定义多层感知机模型
def create_mlp(hidden_layer_sizes=(3,), activation='relu', solver='sgd', random_state=None):
    return MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, activation=activation, solver=solver, random_state=random_state)

# 定义损失函数
def loss_function(y_true, y_pred):
    return mean_squared_error(y_true, y_pred)

# 生成随机样本
def generate_random_samples(n_samples, n_features, noise=0.1):
    X = np.random.rand(n_samples, n_features)
    y = 0.243 * X[:, 0] - 0.220 * X[:, 1] + 0.262 * X[:, 2] +0.246 + noise * np.random.randn(n_samples)
    return X, y

# 蒙特卡罗模拟
def monte_carlo_simulation(n_simulations, n_samples, n_features, hidden_layer_sizes, activation, solver):
    losses = []
    for i in range(n_simulations):
        # 生成随机样本
        X, y = generate_random_samples(n_samples, n_features)
        
        # 创建并训练模型
        mlp = create_mlp(hidden_layer_sizes=hidden_layer_sizes, activation=activation, solver=solver, random_state=i)
        mlp.fit(X, y)
        
        # 预测并计算损失
        y_pred = mlp.predict(X)
        loss = loss_function(y, y_pred)
        losses.append(loss)
    
    return losses

# 参数设置
n_simulations = 100
n_samples = 1000
n_features = 3
hidden_layer_sizes = (3,)
activation = 'relu'
solver = 'sgd'
plt.figure(figsize=(12,3))
# 运行蒙特卡罗模拟
losses = monte_carlo_simulation(n_simulations, n_samples, n_features, hidden_layer_sizes, activation, solver)

# 统计分析
mean_loss = np.mean(losses)
std_loss = np.std(losses)

# 打印结果
print(f'Mean Loss: {mean_loss}')
print(f'Standard Deviation of Loss: {std_loss}')

n, bins, patches = plt.hist(losses, bins=20, edgecolor='none', alpha=0.5,color='lightblue')

# 创建渐变色映射
norm = Normalize(vmin=min(bins), vmax=max(bins))
cmap = plt.get_cmap('viridis')

# 设置每个条形的边缘颜色
for bin_edge, patch in zip(bins, patches):
    color = cmap(norm(bin_edge))
    patch.set_edgecolor(color)
    patch.set_linewidth(1.5)

# 显示图形

plt.xlabel('Losses')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()