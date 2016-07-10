之前已经在服务器上部署过了一个 Flask 现在又写了一个 Django 博客，也需要部署上去，现在就是多Web应用部署。  
  
多Web部署前面几步都和以前一样，主要需要在意的地方是Nginx。  
下面是我部署的部分配置和过程。 
未做详细注解，仅供自己以后参考。  
  
[uWSGI官方文档](http://uwsgi-docs.readthedocs.io/en/latest/)  
[`supervisor`官方文档](http://supervisord.org/)  


### 部署`uWSGI`  
  
uWSGI配置一般直接放在项目文件目录下，在项目目录下创建 `config.ini`  
  

```
[uwsgi]
# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:8080

# 外网访问端口，如果直接用uWSGI外网，这里由于使用了Nginx，故注释掉
# http= :5000

# 指向网站目录
chdir = /root/myweb/Z/

# 处理器数
processes = 4

# 线程数
threads = 2

# 开启python对线程的支持
enable-threads=True

#状态检测地址
stats = 127.0.0.1:8081

module= config.wsgi
master=True
vacuum=True
max-requests=5000
```  
  
### 配置 `supervisor`  
  

之前部署都是在默认配置里直接修改的，后来才发现有更加优雅的方法。  
原来部署Flask时，还什么都不懂，找了很多资料发现大多数都行不通，这次明白了，主要是 `supervisor` 的配置文件名一直在变，不知道是因为不同系统还是确实是这个软件的问题。  
不过到目前为止不变的是它得到配置文件都在`\etc`下。  
打开 `\etc\supervisord.conf`，拉倒最后一行，找到 `files = supervisord.d/*.ini`，所以如果不想直接修改配置文件的一个方法就是将这个项目的supervisor以.ini结尾的配置文件放入`\etc\supervisord.d\`文件夹下。

`Z_supervisor.ini`  
  
```
# 将本文件放入`\etc\supervisord.d\`文件夹下，然后重启supervisor
# 或者保存文件位置不变，重启后`supervisorctl -c pathtofile`
[program:Z]
command=uwsgi /root/myweb/Z/config.ini
directory=/root/myweb/Z
user=root
autostart=true
autorestart=true
stdout_logfile=/root/myweb/Z/uwsgi_supervisor.log
```
  
可能会有写不能顺利进行，但是大概思路是这样。  


### 配置Nginx  
配置Nginx时有两个问题，一个是多server，一个是Django的静态文件
1. server配置  
  
**未完待续**