from mxnet import np,npx
npx.set_np()

'''
features:[growing stock, above stock, underground stock, dead wood, soil carbon sink]
'''
def temperate_dataset(num_samples):
    base_features = np.array([
        [66.7088, 51.6417, 13.4338, 10.1629, 1.6546], # 1990年样本
        [69.7614, 54.5422, 14.2994, 10.6553, 1.4689], # 2000年样本
        [74.5795, 55.7199, 14.3063, 11.2257, 1.2960], # 2010
        [81.6808, 60.7482, 15.5068, 12.278, 1.2364],
        [82.0286, 61.7575, 15.7536, 12.4965, 1.2238],
        [83.6692, 62.5177, 15.9280, 12.3869, 1.2130],
        [84.3697, 63.2645, 16.0948, 12.2792, 1.2025],
        [85.7402, 63.9940, 16.2633, 12.1734, 1.1921],
        [87.2387, 64.7155, 16.4289, 12.0694, 1.1819]
    ])
    base_labels = np.array([36.5787, 38.6496, 39.4945, 43.0397, 43.7541, 44.1543, 44.5567, 44.9476, 45.7179])
    
    features = np.zeros((num_samples, base_features.shape[1]))
    labels = np.zeros(num_samples)

    for i in range(num_samples):
        index = i % base_features.shape[0]
        features[i] = base_features[index] + np.random.normal(0,0.01,base_features.shape[1]) # 手动添加噪声来扩充数据集。
        labels[i] = base_labels[index] + np.random.normal(0,0.01)
    return features, labels

'''
features:[above stock, underground stock, dead wood, soil carbon sink]
'''
def tropical_dataset(num_samples):
    base_features = np.array([
        [163.6042, 39.0687, 10.4195, 41.8219], # 1990年样本
        [166.2991, 39.6593, 10.4816, 41.6476], # 2000年样本
        [169.4436, 40.2601, 10.4921, 41.2532], # 2010
        [171.0793, 40.6087, 10.4523, 41.3681],
        [171.1456, 40.6235, 10.4440, 41.3524],
        [171.1316, 40.6228, 10.4381, 41.3125],
        [171.4636, 40.6909, 10.4344, 41.3500],
        [171.6872, 40.8154, 10.4330, 41.3602],
        [171.9210, 40.7860, 10.4333, 41.3710]
    ])
    base_labels = np.array([148.7436, 150.2905, 151.9677, 153.0506, 153.0616, 152.9963, 153.2461, 153.3993, 153.5628])
    
    features = np.zeros((num_samples, base_features.shape[1]))
    labels = np.zeros(num_samples)

    for i in range(num_samples):
        index = i % base_features.shape[0]
        features[i] = base_features[index] + np.random.normal(0,0.01,base_features.shape[1]) # 手动添加噪声来扩充数据集。
        labels[i] = base_labels[index] + np.random.normal(0,0.01)
    return features, labels

'''
features:[growing stock, above stock, underground stock, dead wood, soil carbon sink]
'''
def polar_dataset(num_samples):
    base_features = np.array([
        [136.7473, 95.09, 23.47, 41.35, 82.21], # 1990年样本
        [136.0558, 94.64, 23.34, 39.96, 82.50], # 2000年样本
        [131.0303, 91.16, 22.57, 40.89, 85.79], # 2010
        [130.0541, 90.49, 22.39, 40.27, 82.94],
        [129.9638, 90.43, 22.37, 40.09, 82.96],
        [129.9778, 90.43, 22.37, 40.09, 82.96],
        [129.9919, 90.43, 22.37, 40.09, 82.96],
        [130.0060, 90.43, 22.37, 40.09, 82.96],
        [130.0200, 90.43, 22.37, 40.09, 82.96]
    ])
    base_labels = np.array([210.01, 209.84, 211.82, 208.01, 207.88, 207.88, 207.88, 207.88, 207.88])
    
    features = np.zeros((num_samples, base_features.shape[1]))
    labels = np.zeros(num_samples)

    for i in range(num_samples):
        index = i % base_features.shape[0]
        features[i] = base_features[index] + np.random.normal(0,0.01,base_features.shape[1]) # 手动添加噪声来扩充数据集。
        labels[i] = base_labels[index] + np.random.normal(0,0.01)
    return features, labels


