import numpy as np

# 给定的数据
values = np.array([
7.12,
11.11,
9.19,
26.31,
27.43,
43.91,
39.06,
53.38,
53.95,
72.38,
86.87,
52.16 ,
134.34,
126.34,
157.37,
197.20 ,
174.70 ,
203.35,
255.89,
211.02,
327.05 ,







])

# 归一化处理
min_val = np.min(values)
max_val = np.max(values)
normalized_values = (values - min_val) / (max_val - min_val)

# 打印结果
print(normalized_values)