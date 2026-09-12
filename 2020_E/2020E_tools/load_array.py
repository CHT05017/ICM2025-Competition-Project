import mxnet
def LoadArray(data_arrays, batch_size, is_train=True):
    dataset = mxnet.gluon.data.ArrayDataset(*data_arrays)
    return mxnet.gluon.data.DataLoader(dataset, batch_size, shuffle=is_train)
