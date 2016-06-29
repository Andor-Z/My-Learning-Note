## 疑问  
- ?class Meta



## 常用命令  
- 创建项目`project`  
`django-admin startproject test_web_1`  

- 创建应用`app`
python manage.py startapp polls

- `python manage.py runserver 8080`   
启动项目，在8080端口。  

- `python manage.py runserver 0.0.0.0:8000`  
在其他电脑上可访问  

- `python manage.py createsuperuser`  
创建admin用户




### 数据库命令  
- `python manage.py migrate`  
migrate查看INSTALLED_APPS设置并根据mysite/settings.py文件中的数据库设置创建任何必要的数据库表，数据库的迁移还会跟踪应用的变化。 

- `python manage.py makemigrations <new_app>`  
创建迁移文件  
告知Django已对models进行更改、Django将这些更改 存储为迁移文件。**未更改数据库**。 

- `python manage.py sqlmigrate app 0001`  
查看迁移文件的SQL语句。
接受参数为迁移文件的编号，然后返回迁移文件的SQL语句。 
但`sqlmigrate`命令并没有真正运行迁移文件 —— 它只是把Django 认为需要的SQL打印出来。  

- `python manage.py migrate`  
利用迁移文件，同步数据库和models。  
找出未被应用的迁移文件，运行在数据库上。  

- `python manage.py check`  
检查项目中的模型是否存在问题

## 部署  
- `python manage.py collectstatic`  
部署时收集静态文件

## 一些小知识点  
- `os.path.dirname()`  
获取文件**所在目录**的完整路径。  
若是目录，则获取目录的父目录的完整路径。  
```
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 返回所在文件的目录的父目录路径
```  
- 默认的设置文件settings.py配置了一个DjangoTemplates后端，其中将APP_DIRS选项设置为True。按照惯例，DjangoTemplates在 INSTALLED_APPS所包含的每个应用的目录下查找名为"templates"子目录。