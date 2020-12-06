# 使用 matplotlib 绘制折线图和散点图

import matplotlib.pyplot as plt


def main():
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
    plt.scatter(x_values, y_values) # 使用 scatter 为散点图，使用 plot 为折线图
    plt.show()


if __name__ == '__main__':
    main()
