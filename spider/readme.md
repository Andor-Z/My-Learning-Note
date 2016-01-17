## Python爬虫实战四之抓取淘宝MM照片
[教程原文地址](http://cuiqingcai.com/1001.html)

原文作者2015.8.2时表示原代码已经不能用了，这片教程只提供学习思路。  
我仍想尝试一下。
* 最开始我使用的是淘女郎的美人库网址（https://mm.taobao.com/search_tstar_model.htm），然后发现依旧是动态网址，这个网址用urllib库不能返回完整的的信息。也就是中间最重要的美美信息不能加载：` <div class="loading J_Loading">数据加载中...</div>`。  
* 继续使用原作者提供的网址，原作者表示之所以原代码不可用是无法