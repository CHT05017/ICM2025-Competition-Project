from mxnet import np,npx
npx.set_np()

'''
features:[Pesticide, Fertilizer, others]
'''
def IM_dataset(num_samples):
    base_features = np.array([
        [1.47, 85.92, 1.47],  # 样本1
        [1.48, 87.25, 1.47],  # 样本2
        [1.49, 90.21, 1.48],  # 样本3
        [1.55, 93.11, 1.56],
        [1.65, 97.82, 1.62],
        [1.66, 97.95, 1.69],
        [1.66, 100.84, 1.67],
        [1.83, 105.41, 1.86],
        [1.86, 99.87, 1.89],
        [1.79, 99.99, 1.88],
        [1.98, 109.77, 2.03],
        [1.98, 113.33, 2.00],
        [2.08, 112.32, 1.89],
        [2.10, 114.30, 2.15],
        [2.10, 117.00, 2.14],
        [2.12, 115.43, 2.16],
        [2.19, 115.93, 2.23],
        [2.14, 118.81, 2.20],
        [2.13, 117.74, 2.18],
        [2.18, 114.75, 2.25],
        [2.19, 120.95, 2.22],
        [2.26, 119.62, 2.29]
    ])
    base_labels = np.array([
12.2,
14.3,
16.52,
18.87,
20.25,
20.1,
22.3,
24,
23.6,
24.8,
25.1,
27.2,
26.1,
27.7,
29.2,
27.4,
28.7,
30,
28.9,
30.01,
32.1,
28.8,




])
    
    features = np.zeros((num_samples, base_features.shape[1]))
    labels = np.zeros(num_samples)

    for i in range(num_samples):
        index = i % base_features.shape[0]
        features[i] = base_features[index] + np.random.normal(0,0.01,base_features.shape[1]) # 手动添加噪声来扩充数据集。
        labels[i] = base_labels[index] + np.random.normal(0,0.01)
    return features, labels

