2016年2月22日13:35:00  

#Pandas-cookbook_note

中文教程地址[Pandas-cookbook](https://github.com/ia-cas/pandas-cookbook)

## IPython Notebook概览  

`Shift + Tab` 查看函数文档信息

## 1. 从 csv 文件中读取数据

* 读取数据`pd.read_csv`中的问题
    1、`sep=';'`字段分隔默认为; 还是现在能自动匹配字段分隔符？
    2、`encoding='latin1'` 默认编码'utf8'出来的文字是正确的，反而使用了'latin1'编码后显示不正常了。

* plot画图问题
`_ = fixed_df['Berri 1'].plot()` 出现`code above will lead to AttributeError: Unknown property color_cycle`的问题。
解决办法：[Stack Overflow AttributeError: Unknown property color_cycle](http://stackoverflow.com/questions/33995707/attributeerror-unknown-property-color-cycle)
大神表示这个是在pandas 0.17.1和Matplotlib1.5.0版本下的一个bug。解决办法是将
```
import pandas as pd 
pd.set_option('display.mpl_style', 'default')
```
改成
```
import matplotlib
matplotlib.style.use('ggplot')
```
PS：我是直接添上这两句了。ggplot不是R语言里的吗？


* 主要代码
```
# Render our plots inline
%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

# Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)


broken_df = pd.read_csv('.\pddata\2012.csv')


df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
_ = df['Berri 1'].plot()
```


## 2、选择和查找数据

* 计数
complaints['Complaint Type'].value_counts()

* 直方图
_ = complaint_counts[:10].plot(kind='bar')

## Chapter 3: “哪个区抱怨噪声的人最多？”(查找数据进阶) 


## Chapter 4: 用groupby和agg操作来查找人们骑自行车最多的一天是星期几 

使用的是2015年的数据，根据[song_cai_csdn-pandas Cookbook--Chapter 1](http://blog.csdn.net/caisong/article/details/50678437)说需要把00:00这一行进行处理，本来以为是会出现详细的时间，实际操作后，只是把那一行删除了。

* 还有`dafirst = True` 参数实际操作中并未发现什么区别



# The usual preamble
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)


# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)