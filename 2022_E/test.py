import numpy as np
import pandas as pd

# 已知数据
years = np.array([1990, 2000, 2010, 2015, 2020])
values = np.array([348272.93, 347801.97, 347322.21, 347115.71, 346928.1])

# 创建DataFrame
df = pd.DataFrame({'Year': years, 'Value': values})

# 使用线性插值法预测缺失值
df = df.set_index('Year').reindex(range(1990, 2021)).interpolate(method='linear')

# 获取预测值
predicted_values = df.loc[2016:2019]

print(predicted_values)