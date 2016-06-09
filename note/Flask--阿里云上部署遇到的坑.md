# Flask--阿里云ECS上部署遇到的坑  

## 背景  
原则：快速，不折腾，尽量在最短的时间内，让web跑起来。
### ECS配置  
CPU  1核  
内存 1G  
系统 CentOS 7.0 64位  
  
### 部署背景  
Flask + Mysql + github  
只在自己本地虚拟机中玩的Ubuntu

## 坑！！！  

### 第一个大坑：阿里云！！  
其实最开始我买来的系统是Ubuntu 并不是CentOS的。  
- MySql 安装不上  
主机到手后

- pyenv  
 pip install -r requirements/dev.txt
- git ssh key  
- pip
- export 环境变量



### 配置 uwsgi
[uWSGI官方文档](http://uwsgi-docs.readthedocs.io/en/latest/)
[阿里云部署 Flask + WSGI + Nginx 详解](http://www.cnblogs.com/Ray-liang/p/4173923.html)  
刚开始是根据这篇文章部署，但是出现两个问题：  
1. 指向网站目录的`chdir`制定不到对的位置，不管是绝对路径还是相对路径。遵循快速原则，直接注释掉了这个变量，呆以后再找出正确写法。  
2. 外网无法访问。在这里找到：[Nginx+uWSGI安装与配置-DBA的罗浮宫](http://mdba.cn/2013/10/18/nginxuwsgi%e5%ae%89%e8%a3%85%e4%b8%8e%e9%85%8d%e7%bd%ae/)   
也就是添加`http`变量。  



[nginx启动，重启，关闭命令](http://www.cnblogs.com/derekchen/archive/2011/02/17/1957209.html)




### 安装SUpervisor  

supervisord    //启动supervisor

supervisorctl   //打开命令行

[root@vm14211 ~]# supervisorctl 
redis                            RUNNING    pid 24068, uptime 3:41:55

ctl中： help   //查看命令

ctl中： status  //查看状态

或者  

supervisorctl status  //查看状态  

supervisorctl stop [进程名]   //停止

supervisorctl start [进程名]



[supervisor - Python进程管理工具](http://chenxiaoyu.org/2011/05/31/python-supervisor.html) 
[按需讲解之Supervisor](http://www.cnblogs.com/yjf512/archive/2012/03/05/2380496.html)

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
