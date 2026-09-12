import matplotlib.pyplot as plt
from IPython import display

'''Jupyter Notebook中高清显示'''
def use_svg_display():
    display.set_matplotlib_formats('svg')


'''设置由matplotlib生成的图表的轴的属性'''
def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    if legend:
        axes.legend(legend)
    axes.grid()
    

'''使用程序类animator 用于观测画图'''
    
class Animator:
    def __init__(self,xlabel=None, ylabel=None, legend=None, xlim=None, ylim = None, xscale='linear',yscale='linear',fmts=('-','m--','g-','r:'),rows_num=1,cols_num=1,figsize=(3.5,2.5)):
        if legend is None:
            legend = []
        use_svg_display()
        self.fig, self.axes = plt.subplots(rows_num,cols_num,figsize = figsize) # 因为subplots返回的是由figure 和 axes组成的数组。其中figure是整个画布，axes是每个子图
        if rows_num * cols_num == 1:
            self.axes = [self.axes, ]
        # 用lambda表达式捕获参数
        self.config_axes = lambda: set_axes(self.axes[0],xlabel,ylabel,xlim,ylim,xscale,yscale,legend) 
        self.X, self.Y, self.fmts = None, None, fmts
    
    def add(self,x,y):
        '''向图表中添加多个数据点. 当需要同时绘制多条曲线时，将y定义成一个元组, 元组中的每个元素都是希望作图的对象；当需要做多张图的时候可以用+来连接多个元组作为第二个参数'''
        if not hasattr(y, "__len__"): # 通过检查y是否包含长度属性来判断y是否为可迭代对象
            y = [y]
        n = len(y)
        if not hasattr(x,"__len__"):
            x = [x] * n # 将x转换成包含n个相同元素的列表（作为横坐标）
        if not self.X: # 如果self.X为空，则将X初始化为包含n个空列表的列表
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a,b) in enumerate(zip(x,y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].cla() # 清除当前子图
        for x,y,fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(x,y,fmt)
        self.config_axes()
        display.display(self.fig)
        display.clear_output(wait=True)

'''
# Jupyter Notebook 代码示例

animator = Animator(xlabel='epochs',ylabel='losses',yscale = 'log', xlim=[0,100],legend=['train','test'])

for epoch in range(epochs)
    # 训练代码
    animator.add(epoch+1,(EvaluateLoss(model, train_loader,loss_func), EvaluateLoss(model, test_loader, loss_func)))


'''
