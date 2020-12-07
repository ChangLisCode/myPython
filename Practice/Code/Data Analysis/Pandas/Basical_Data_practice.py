import numpy as np
import pandas as pd
 
# Pandas应用
# 练习用的数据
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 从具有索引标签的字典数据创建一个DataFrame 的 df
df = pd.DataFrame(data,index = labels)

# 返回DataFrame的前三行，显示结果基于head的定义
df.iloc[:3]
df.head(3)

# Numpy 应用，从 numpy 数组，构造DataFrame

# 定义数据
df2 = pd.DataFrame(np.array([[1, 2, 3,5], [4, 5, 6,5], [7, 8, 9,5]]),
                    columns=['a', 'b', 'c','d'])
#运行
df2

# 通过其他DataFrame,来创建DataFrame df3
df3 = df2[["a","b","c"]].copy()
df3

# 从csv文件中,每隔n行,来创建Dataframe, 
# n=50
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df2 = pd.DataFrame()
#运行失败

# 用Series创建DataFrame
s_1 = pd.Series(data['animal'])         # 定义行
s_2 = pd.Series(data['age'])            # 定义行
s_3 = pd.Series(data['visits'])         # 定义行
s_4 = pd.Series(data['priority'])       # 定义行
pd_2 = pd.DataFrame([s_1,s_2,s_3,s_4])  # 创建DataFrame，使用定义的行
pd_2                                    # 运行

'''
# pandas处理NaN值
dropna(axis=, how=)：丢弃NaN数据，{axis：0(按行丢弃)，1(按列丢弃)} {how：'any'(只要含有NaN数据就丢弃)，'all'(所有数据都为NaN时丢弃)}

fillna(value=)：将NaN值都设置为value的值

isnull()：对每各元素进行判断是否是NaN，返回结果矩阵

np.any(matrix) == value：判断matrix矩阵中是否有value值

np.all(matrix) == value：判断matrix矩阵中是否所有元素都是value值
# 失败
'''

# pandas读取数据、导出数据
# 根据数据的格式，pandas提供了多种数据读取和导出的方法，如：
# 读取数据：read_csv、read_table、read_fwf、read_clipboard、read_excel、read_hdf
# 导出数据：to_csv、to_table、to_fwf、to_clipboard、to_excel、to_hdf

df = pd.read_csv('Q1.csv')
print(df)
df.to_csv('Q1_pandas.csv')
# 失败

# pandas合并数据
concat方法是拼接函数，有行拼接和列拼接，默认是行拼接，拼接方法默认是外拼接(并集)，拼接对象是pandas数据类型。
第一个参数：需要合并的矩阵
axis：合并维度，0：按行合并，1：按列合并
join：处理非公有 列/行 的方式，inner：去除非公有的 列/行，outer：对非公有的 列/行 进行NaN值填充然后合并
ignore_index：是否重排行索引

df1 = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'], index=[0, 1, 2])
df2 = pd.DataFrame(np.ones((3, 4)), columns=['B', 'C', 'D', 'E'], index=[1, 2, 3])
print(pd.concat([df1, df2], join='outer', ignore_index=True)) # join = {'outer', 'inner'}
print(pd.concat([df1, df2], axis=1, join_axes=[df1.index]))
print(df1.append([df2], ignore_index=True))
#失败

# append方法在index方向连接两个DataFrame或者对DataFrame进行扩展
# append 方法可以直接用list对DataFrame进行扩展。
# append方法并不能像list的append方法一样对原来的df继续修改，而是建立了一个新的对象。如果要修改df，那么需要重新对df赋值，所以append的方法执行效率并不是很高。
df = pd.DataFrame([[1, 2], [3, 4]])
df = df.append([[1,2]]) #添加一行，为何序号没有自动顺延？
print(df)

# 将两个DataFrame连接起来
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df = df.append(df2)     #添加一行，为何序号没有自动顺延？
print(df)

# Join方法 是基于Index连接DataFrame，连接方法有inner内连接（基于并截止于新加入的序列，、outer外连接（基于并截止于caller序列）、left左连接（基于原有的caller序列）、right右连接（基于新加入的序列）
caller = pd.DataFrame({'key':['A0','A1','A2','A3','A4','A5'],'B':['B0','B1','B2','B3','B4','B5']})
other = pd.DataFrame({'key':['A0','A1','A2'],'C':['C0','C1','C2']})
caller.join(other,lsuffix='_caller',rsuffix='_other',how='outer')

# merge方法，与Join方法类似，不过语法略有不同。连接方法有inner内连接（基于并截止于新加入的序列，、outer外连接（基于并截止于caller序列）、left左连接（基于原有的caller序列）、right右连接（基于新加入的序列）
df = pd.merge(caller,other,on = ['key'],how = 'inner')