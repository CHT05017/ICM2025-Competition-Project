from mxnet import np,npx
npx.set_np()

'''
features:[RW,IW,LW]
'''
def PPMLP_datasets(num_samples):
    base_features = np.array([
        [5.78,	16.98	,92.77], # 1990年样本
        [6.53,	18.57,	96.07], # 2000年样本
        [7.44,	20.53,	100.72], # 2010
        [8.38	,22.51	,104.93],
        [9.46,	24.74,	109.80 ],
        [10.49,	26.83,	113.53],
        [11.72,	29.33,	118.5],
        [13.05,	32.01,	123.7],
        [13.92,	33.59,	124.44],
        [15.15,	35.93,	127.75],
        [16.87,	39.28,	134.1],
        [18.45,	42.22,	138.48],
        [19.97,	45.02,	142.18],
        [21.61,	48.10 ,	146.4],
        [23.21,	51.00, 	149.74],
        [25.17,	54.34,	154.54],
        [27.00, 	57.79,	159.26],
        [28.95	,61.50 ,	163.77],
        [30.93,	65.31,	168.32],
        [32.83,	67.31,	173.84],
        [34.29,	68.04,	177.01]
    ])
    base_labels = np.array([115.53, 121.17, 128.69, 135.82, 144, 150.85, 159.55, 168.76, 171.95, 178.83, 190.25, 199.15, 207.17, 216.11, 223.95, 234.05, 244.05, 254.22, 264.56, 273.98, 279.34])
    
    features = np.zeros((num_samples, base_features.shape[1]))
    labels = np.zeros(num_samples)

    for i in range(num_samples):
        index = i % base_features.shape[0]
        features[i] = base_features[index] + np.random.normal(0,0.01,base_features.shape[1]) # 手动添加噪声来扩充数据集。
        labels[i] = base_labels[index] + np.random.normal(0,0.01)
    return features, labels

