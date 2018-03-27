

> 创建虚拟环境
- 下载scrapy

> 创建项目
- 执行代码,会有自己的模板
```
scrapy startproject 工程名
```
![53784234.png](http://p693ase25.bkt.clouddn.com/2018/03/27/597b2571152c2b351499bba1aad8ac6e.png "53784234.png")
- 创建模板
```
scrapy genspider jobbole blog.jobbole.com
```
![55756984.png](http://p693ase25.bkt.clouddn.com/2018/03/27/21cf669a3b79c038f86c7b4933b61e1f.png "55756984.png")
- 启动项目,注意将settings里面的遵守robots协议关闭，不要忘记修改user-agent
```
scrapy crawl 名称
```

- 爬虫文件jobbole.py
    - name:爬虫的名字
    - allowed_domains 是一个列表，允许的域名，你所想抓取的所有url都必须在这个域名列表之下，否则不能爬取
    - 注意： 很多图片网站，图片体质和网址不在一个域名下。
      ![559312.png](http://p693ase25.bkt.clouddn.com/2018/03/27/3e9618983288ed34323ecbe68ea6e76c.png "559312.png")

    - 注意，通过xpath获取到的是对象，就算直接获取属性获取的也是对象，要通过extract（）【0】来提取内容，或者是使用extract_first()函数


- 运行可以直接导出json文件或者是xml文件
```
scrapy crawl 爬虫文件名 -o qiubai.json
```