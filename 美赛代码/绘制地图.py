
'''浮雕图 - 美洲
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 创建 Basemap 实例，设置美国的经纬度范围和投影方式
map = Basemap(llcrnrlon=-135, llcrnrlat=10, urcrnrlon=-10, urcrnrlat=35,
              resolution='i', projection='cass', lat_0=37.5, lon_0=-95)

# 绘制浮雕图像
map.etopo()

# 绘制海岸线
map.drawcoastlines()

# 显示地图
plt.show()


'''

# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


map = Basemap(width=12000000,height=9000000,
            rsphere=(6378137.00,6356752.3142),
            resolution='l',area_thresh=1000.,projection='lcc',
            lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
# 地图边界
#map.drawmapboundary(fill_color='aqua')
# 陆地海洋填充
# map.fillcontinents(color='#00000', lake_color='#00000')
# 国家
map.drawcountries()
# 美洲地图
map.drawstates(color='0.5')
# 绘制海岸线和陆地边界
map.drawcoastlines()
plt.show()


'''
lat, lon = 29.9511, -90.0715  # New Orleans 的经纬度
x, y = map(lon, lat)
map.plot(x, y, 'bo', markersize=2)
plt.text(x, y, ' New Orleans', fontsize=2, ha='left', va='center', color='blue')
'''
'''


plt.show()
'''
'''
# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 创建 Basemap 实例，设置亚洲的经纬度范围和投影方式
map = Basemap(width=12000000, height=9000000,
              rsphere=(6378137.00, 6356752.3142),
              resolution='l', area_thresh=1000., projection='lcc',
              lat_1=45., lat_2=55, lat_0=20, lon_0=80)

# 绘制地图边界
# map.drawmapboundary(fill_color='aqua')

# 填充陆地和海洋颜色
# map.fillcontinents(color='#FF7F50', lake_color='#00BFFF')

# 绘制国家边界
map.drawcountries()

# 绘制州界
map.drawstates(color='0.5')
map.drawcoastlines()

# 添加孟买的标记
lat, lon = 19.0760, 72.8777  # 孟买的经纬度
x, y = map(lon, lat)
#map.plot(x, y, 'bo', markersize=5)
#plt.text(x, y, ' Mumbai', fontsize=12, ha='left', va='center', color='blue')

# 显示地图
plt.show()
'''
'''
'''
'''
印度浮雕
import warnings
warnings.filterwarnings('ignore')

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# 创建 Basemap 实例，设置印度的经纬度范围和投影方式
map = Basemap(llcrnrlon=68, llcrnrlat=6, urcrnrlon=98, urcrnrlat=36,
              resolution='i', projection='cass', lat_0=21, lon_0=78)

# 绘制浮雕图像
map.etopo()

# 绘制海岸线
map.drawcoastlines()

# 显示地图
plt.show()

'''