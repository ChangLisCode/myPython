# 使用 matplotlib 绘制折线图和散点图

import matplotlib.pyplot as plt
import numpy as np

# 绘制直方图
def main():
    # 通过random模块的normal函数产生1000个正态分布的样本
    data = np.random.normal(10.0, 5.0, 1000)
    # 绘制直方图(直方的数量为10个)
    plt.hist(data, 10)
    plt.show()


# 绘制正弦曲线
def main2():
    # 指定采样的范围以及样本的数量
    x_values = np.linspace(0, 2 * np.pi, 1000)
    
    # 一张图一条曲线
    # 计算每个样本对应的正弦值
    #y_values = np.sin(x_values)
    # 绘制折线图(线条形状为--, 颜色为蓝色)
    #plt.plot(x_values, y_values, '--b')
    
    # 一张图，两条曲线
    plt.plot(x_values, np.sin(x_values), '--b')
    plt.plot(x_values, np.sin(2 * x_values), '--r')
    
    # 两个坐标系上绘制出两条曲线
    plt.subplot(2, 1, 1)
    plt.plot(x_values, np.sin(x_values), 'o-b')
    # 设置绘图为2行1列活跃区为2区(第二个图)
    plt.subplot(2, 1, 2)
    plt.plot(x_values, np.sin(2 * x_values), '.-r')

    
    plt.show()


# 绘制折线图+散点图
def main1():
    # 保存x轴数据的列表
    x_values = [x for x in range(1, 11)]
    # 保存y轴数据的列表
    y_values = [x ** 10 for x in range(1, 11)]
    # 设置图表的标题以及x和y轴的说明
    plt.title('Square Numbers2') # 图表名称
    plt.xlabel('Value', fontsize=11)   # X轴名称字号
    plt.ylabel('Square', fontsize=11)   # y轴名称字号
    # 设置刻度标记的文字大小
    plt.tick_params(axis='both', labelsize=6)
    # 绘制折线图
    plt.plot(x_values, y_values,'xy') # 使用 scatter 为散点图，使用 plot 为折线图
    # 其中参数'xr'表示每个点的记号是‘x’图形，颜色是红色（red）。蓝色为‘xb’，黄色‘xy’
    
    plt.show()


if __name__ == '__main__':
    main()

