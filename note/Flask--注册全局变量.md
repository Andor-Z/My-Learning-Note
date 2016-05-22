# Flask中注册全局变量 
2016年5月21日  
## Problem  
在《Flask Web Development》中每一个模板的title都是手动写的Flasky，总是觉得这样是不科学的。Flask中声明全局变量的方法？  

## Solution 
### 1.context processor (上下文处理器、环境处理器)  
其实书中在关于角色权限认证, 全局使用`Permission`类的那一节已经写过一种方法了，叫做**上下文处理器**。书中是这样写的：   
`app/main/__init__.py:`
```python
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
```
Flask中有应用(app)和蓝图(Blueprint)，一般来说在不同情形下会使用不同的函数：

- app
**[`Flask.context_processor(*args, **kwargs)`](http://flask.pocoo.org/docs/0.10/api/#flask.Flask.context_processor)**  

-  蓝图(Blueprint)  
**[`Blueprint.context_processor(f)`](http://flask.pocoo.org/docs/0.10/api/#flask.Blueprint.context_processor)**:只能本蓝图内使用  
**[`Blueprint.app_context_processor(f)`](http://flask.pocoo.org/docs/0.10/api/#flask.Blueprint.app_context_processor)**：可以全局使用    
在每个request中都可以使用，也就是在此蓝图外也可以使用  
用法和书中`Permission`实现方法一样。通过装饰器注册。  

context processor 不仅可以注册变量，还可以注册函数：  
```python
@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)
```

### 2.add template global  添加到jinja的全局名称空间中
**[`Flask.add_template_global(*args, **kwargs)`](http://flask.pocoo.org/docs/0.10/api/#flask.Flask.add_template_global)** : app中使用
**[`Blueprint.add_app_template_global(f, name=None)`](http://flask.pocoo.org/docs/0.10/api/#flask.Blueprint.add_app_template_global)**:蓝图使用  

使用方法：  
`app.add_template_global(Permission, 'Permission')`   

### 3.使用全局变量**g**  
```python
from ..models import Permission
from flask import g

g.Permission = Permission
```
  





参考：  
[Flask把变量注册到模板中](http://www.cnblogs.com/StitchSun/p/5396033.html)
[Jinja模板-环境处理器](http://dormousehole.readthedocs.io/en/latest/templating.html#id6)


Flask中注册全局变量  
Flask中声明全局变量   
Flask中注册变量到模板  