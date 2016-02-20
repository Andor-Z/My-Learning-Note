##4个顶级文件夹：
* app:Flask程序
    - app/models.py 数据库模型
    - app/email.py 电子邮件支持函数
* migrations: 数据库迁移脚本
* tests: 单元测试编写
* venv

* requirements.txt 列出了所有依赖包
* config.py 储存配置
* manage.py 用于启动其他的程序任务





### 细小知识点

* 设置环境变量：

Mac Linux ：
`$ export MAIL_USERNAME = <flaskm@example.com>`


Windows :
`(venv) > set MAIL_USERNAME = <flaskm@example.com>`


* 获取环境变量：
```
import os
os.environ.get('MAIL_USERNAME')
```

* 导出依赖包及其版本  
`(venv) > pip freeze >requirements.txt`  

* 安装依赖包
`(venv) > pip intall -r requirements.txt`


### 疑难杂症

* Python 虚拟环境下 使用pip 安装新包 出现`Fatal error in launcher: Unable to create process using`
    解决办法：
            Windows环境下使用：
        python -m pip install xxx来替换 install xxx；







* [python中 from . import ×××的那个点](https://www.zhihu.com/question/28688151)

* [4、视图函数中的表单操作](https://segmentfault.com/a/1190000002172627)