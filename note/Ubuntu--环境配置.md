# 更改语言。 在下载中文包和应用中文包后，把中文选项用鼠标拖到最顶上。
# 输入法：[搜狗输入法 for linux](http://pinyin.sogou.com/linux/)
    - 暂时无法使用，根据很多教程表示在Ubuntu14版本后，可以直接安装就可以了，不知道为何我的还是不行。
# Python 版本管理。
    - [pyenv](https://github.com/yyuu/pyenv#installation)
    - [Linux 下的 Python 多版本管理（pyenv）](http://my.oschina.net/lionets/blog/267469#OSC_h3_7)
    - [Python多版本切换工具-Pyenv\virtualenv及Anaconda科学计算环境的配置](https://segmentfault.com/a/1190000004020387?utm_source=tuicool&utm_medium=referral#articleHeader12)
    - 注意：
        1. 由于教程都是说直接git 到根目录下，但其实根目录是`/home/<user>`，但是环境变量`PYENV_ROOT=$HOME/.pyenv`两个目录不是同一个。故我自作聪明，自己安装时，修改了其中之一，导致安装不成功。
        2. 通过`pyenv install`安装，速度非常非常慢！！不知道是不是我的个例。 

# sublime text 3
- 安装
```
$ sudo add-apt-repository ppa:webupd8team/sublime-text-3
$ sudo apt-get update
$ sudo apt-get install sublime-text-installer
```
- Package Control
ctrl+`
```
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```