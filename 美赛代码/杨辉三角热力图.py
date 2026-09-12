# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# 创建 Basemap 实例，设置美国的经纬度范围和投影方式
map = Basemap(width=12000000, height=9000000,
              rsphere=(6378137.00, 6356752.3142),
              resolution='l', area_thresh=1000., projection='lcc',
              lat_1=45., lat_2=55, lat_0=50, lon_0=-107.)

# 绘制地图边界
map.drawmapboundary(fill_color='aqua')

# 绘制海岸线和陆地边界
map.drawcoastlines()

# 绘制国家边界
map.drawcountries()

# 绘制州界
map.drawstates(color='0.5')

# 添加 New Orleans 的标记
lat, lon = 29.9511, -90.0715  # New Orleans 的经纬度
x, y = map(lon, lat)
map.plot(x, y, 'bo', markersize=5)
plt.text(x, y, ' New Orleans', fontsize=12, ha='left', va='center', color='blue')

# 生成示例数据（100x100的二维矩阵）
data = np.array([
    [1, 4, 7, 14, 21, 28, 35, 35, 35, 28, 21, 14, 7, 4, 1],
    [4, 1, 4, 6, 11, 15, 17, 20, 17, 15, 11, 6, 4, 1, 4],
    [7, 4, 1, 3, 5, 8, 10, 10, 10, 8, 5, 3, 1, 4, 7],
    [14, 6, 4, 1, 3, 4, 5, 6, 5, 4, 3, 1, 3, 6, 14],
    [21, 13, 5, 3, 1, 2, 3, 3, 3, 2, 1, 3, 5, 13, 21],
    [28, 15, 10, 4, 3, 1, 2, 2, 2, 1, 3, 4, 10, 15, 28],
    [35, 23, 10, 7, 3, 2, 1, 1, 1, 2, 3, 7, 10, 23, 35],
    [35, 20, 13, 6, 4, 2, 2, 1, 2, 2, 4, 6, 13, 20, 35],
    [35, 23, 10, 7, 3, 2, 1, 1, 1, 2, 3, 7, 10, 23, 35],
    [28, 15, 10, 4, 3, 1, 2, 2, 2, 1, 3, 4, 10, 15, 28],
    [21, 13, 5, 3, 1, 2, 3, 3, 3, 2, 1, 3, 5, 13, 21],
    [14, 6, 4, 1, 3, 4, 5, 6, 5, 4, 3, 1, 3, 6, 14],
    [7, 4, 1, 3, 5, 8, 10, 10, 10, 8, 5, 3, 1, 4, 7],
    [4, 1, 4, 6, 11, 15, 17, 20, 17, 15, 11, 6, 4, 1, 4],
    [1, 4, 7, 14, 21, 28, 35, 35, 35, 28, 21, 14, 7, 4, 1]
])

# 创建一个Figure对象和一个子图
fig, ax = plt.subplots()

# 绘制热力图，并设置样式
heatmap = ax.imshow(data, cmap='hot', interpolation='nearest', aspect='auto')

# 添加颜色条
cbar = plt.colorbar(heatmap, fraction=0.046, pad=0.04)

# 添加图例
ax.set_title('heat_map', fontsize=16, fontweight='bold')

# 添加横纵坐标label
ax.set_xlabel('X', fontsize=14, fontweight='bold')
ax.set_ylabel('Y', fontsize=14, fontweight='bold')

# 设置颜色条标签字体大小
cbar.ax.tick_params(labelsize=12)

# 设置横纵坐标标签字体大小
ax.tick_params(axis='both', which='major', labelsize=12)

# 设置背景颜色
ax.set_facecolor('#f0f0f0')

# 设置图表边框颜色
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

# 显示图形
plt.tight_layout()
plt.show()