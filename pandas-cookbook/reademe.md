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




# Render our plots inline
%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.rcParams['figure.figsize'] = (15, 5)


broken_df = pd.read_csv('.\pddata\2012.csv')
