import numpy as np
import matplotlib.pyplot as plt

# 定义参数
months = np.arange(1, 36.1, 0.1)  # 使用更精细的时间步长以获得平滑曲线，覆盖5年

# 模拟环境因素影响（温度、降水、日照时长）
temperature_effect = np.sin((months - 3) * np.pi / 6)  # 假设最热在7月，每12个月重复一次
precipitation_effect = np.cos((months - 9) * np.pi / 6)  # 假设降水高峰在9月，每12个月重复一次
daylight_effect = np.sin((months - 6) * np.pi / 6)  # 日照时长变化，假设最长在6月，每12个月重复一次

# 引入额外影响因素（例如病虫害爆发、极端天气等）
random_fluctuations = 0.2 * np.random.randn(len(months))  # 添加随机波动
extreme_weather_events = np.zeros(len(months))
for year in range(5):
    # 随机选择某些月份作为极端天气事件的发生点
    extreme_months = np.random.randint(1, 13, 3) + year * 12
    for month in extreme_months:
        idx = np.where(np.abs(months - month) < 0.5)[0]
        if len(idx) > 0:
            extreme_weather_events[idx] += 0.5

# 农业活动因子：播种期和收获期（使用高斯分布来模拟这些活动的影响）
def gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((np.mod(x - 1, 12) + 1 - mu) / sigma) ** 2)

agriculture_activities = np.zeros(len(months))
for year in range(5):
    agriculture_activities += gaussian(np.mod(months - 1, 12) + 1, 4, 0.5) + gaussian(np.mod(months - 1, 12) + 1, 9, 0.5)

# 综合所有影响因素
total_effect = (temperature_effect + precipitation_effect + daylight_effect +
                agriculture_activities + random_fluctuations + extreme_weather_events)

# 确保最小值为0.2，并正则化数据以便于比较
min_value = np.min(total_effect)
if min_value < 0.2:
    total_effect -= (min_value - 0.2)
total_effect = (total_effect - np.min(total_effect)) / (np.max(total_effect) - np.min(total_effect))

# 设置最小值为0.2
total_effect = 0.2 + (total_effect - np.min(total_effect)) * (1 - 0.2)

# 绘制连续函数图像
plt.figure()
plt.plot(months, total_effect, linewidth=2, color=[0.2, 0.6, 0.2])
plt.xlabel('Month of the Year')
plt.ylabel('Normalized Impact on Agriculture Ecosystem')
plt.title('Continuous Agricultural Ecosystem Dynamics over Five Years with Additional Factors')
plt.xticks(np.arange(1, 61, 12), ['Jan Y1', 'Jan Y2', 'Jan Y3', 'Jan Y4', 'Jan Y5'])
plt.grid(True)
plt.show()