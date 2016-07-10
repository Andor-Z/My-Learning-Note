
### 背景  
原则：快速，不折腾，尽量在最短的时间内，让web跑起来。
#### ECS配置  
CPU  1核  
内存 1G  
系统 CentOS 7.0 64位  
  
#### 部署背景  
 
之前只在自己本地虚拟机中玩的Ubuntu

### 具体部署、设置和命令  
Flask + Mysql + uWSGI + Supervisor + Nginx   
  

#### Mysql  
其实最开始我阿里云ECS上的是Ubuntu系统。但是Mysql怎么都装不上不管是根据阿里帮助文档上的`update_source`脚本，还是自己编译。总是提示缺少依赖包，然后自己去安装依赖包，又缺少其他的。提交工单找阿里云的售后，阿里的售后要了我的IP和密码，然后他们也搞不定，最后他们和我说，**Mysql是第三方软件，他们只能友情协助，无法提供跟多帮助。**  
  

最终在网上把眼睛都找瞎的了的我，终于找到了正确的安装方式。由于系统的依赖包关系，要用`aptitude`替换`apt-get`安装，一个命令解决了我一整天的瞎忙。  
本来以为终于可以松口气了。但是，阿里云的这个Ubuntu中的Python环境又出问题了。  
  
#### Python环境  
linux上我还是喜欢用`pyenv`，方便。  

上面说到阿里云Ubuntu的Python有问题。第一个是pyenv安装好了后，无法切换Python，总是系统自带的Python。如果仅仅是这样，我也可以换`virtualenv`管理Python版本。但是但是，系统自带的Python3的pip又安装不上了。这两天弄下来真是要崩溃了。然后我发现阿里云是可以自己换系统的，我果断换了据说系统稳定，文档齐全的CentOS。然后天气晴朗了，一路顺风顺水！！  
  
- pyenv  
比较简单，文档也很齐全。主要参考：  
[pyenv官方GitHub](https://github.com/yyuu/pyenv)  
[树莓派（Ubuntu15.04）安装多版本Python](http://www.jianshu.com/p/5c7a9892e60f)  
  
有一点需要注意，就是在重启shell的时候需要加上一个`-l`参数。  

  
- 用Git部署代码  
用的还是GitHub，然后SSh  
  
- `pip install -r requirements/dev.txt`  

- 环境变量  
```
echo 'export SQLALCHEMY_DATABASE_URI="......"' >> ~/.bashrc
....
```

#### 配置uWSGI  
`pip install uwsgi`  
  
- 配置起动uWSGI  
`config.ini`   

```
[uwsgi]

# uwsgi 启动时所使用的地址与端口
socket = 127.0.0.1:8001 

# 外网访问端口，如果直接用uWSGI外网，这里由于使用了Nginx，故注释掉
# http= :5000

# 指向网站目录
chdir = /home/www/ 

# python 启动程序文件
wsgi-file = manage.py 

# python 程序内用以启动的 application 变量名
# app 是 manage.py 程序文件内的一个变量，这个变量的类型是 Flask的 application 类
callable = app 

# 处理器数
processes = 4

# 线程数
threads = 2

#状态检测地址
stats = 127.0.0.1:9191
```
启动命令是在配置文件夹下：`uwsgi config.ini`  
但是我准备使用`Supervisor`，故启动命令仅供测试的时候用。  

[uWSGI官方文档](http://uwsgi-docs.readthedocs.io/en/latest/)  
[阿里云部署 Flask + WSGI + Nginx 详解](http://www.cnblogs.com/Ray-liang/p/4173923.html)   
[Nginx+uWSGI安装与配置-DBA的罗浮宫](http://mdba.cn/2013/10/18/nginxuwsgi%e5%ae%89%e8%a3%85%e4%b8%8e%e9%85%8d%e7%bd%ae/)   
 

#### 配置`Supervisor`  
安装  
`yum install supervisor`  
在全局配置文件`/etc/supervisord.conf`中加入： 
  

```
[program:CM-Web]
# 启动命令入口
command=uwsgi /root/myweb/CM-Web/config.ini

# 命令程序所在目录
directory=/root/myweb/CM-Web
#运行命令的用户名
user=root

autostart=true
autorestart=true
#日志地址
stdout_logfile=/root/myweb/CM-Web/uwsgi_supervisor.log
```
  
```
supervisord    //启动supervisor
supervisorctl   //打开命令行 

命令行中： help   //查看命令

命令行中： status  //查看状态

或者  

supervisorctl status  //查看状态  

supervisorctl stop [进程名]   //停止

supervisorctl start [进程名]
```  

- 注意：  
配置文件地址的修改  
新启动命令添加后，需要在命令行中：`reread`  `update` 再start
[使用 supervisor 管理进程](http://www.ttlsa.com/linux/using-supervisor-control-program/)  
[supervisor - Python进程管理工具](http://chenxiaoyu.org/2011/05/31/python-supervisor.html)  
[按需讲解之Supervisor](http://www.cnblogs.com/yjf512/archive/2012/03/05/2380496.html)  

  
  
#### 配置`Nginx`  

`yum install nginx`  
在配置文件`/usr/local/nginx/conf/nginx.conf`中添加：  

```
server {
        listen       80;
        server_name  公网IP;
        

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            include  uwsgi_params;
            uwsgi_pass 127.0.0.1:8001;  # 指向uwsgi 所应用的内部地址,所有请求将转发给uwsgi 处理
            uwsgi_param UWSGI_CHDIR  /root/myweb/CM-Web; # 指向网站根目录
            uwsgi_param UWSGI_SCRIPT manage:app;  # 指定启动程序
        }
```  
最后重启nginx

[nginx启动，重启，关闭命令](http://www.cnblogs.com/derekchen/archive/2011/02/17/1957209.html) 