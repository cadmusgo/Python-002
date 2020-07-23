# 学习总结
本周主要学习 python 爬虫，分为 1.基本函式库(request,bs4) 2.scrapy 框架
通过两种方式的练习后，觉得使用scrapy框架对后续爬虫的维护有极大的帮助。
通过老师对scrapy框架的详细说明，对整体设计概念有了一定的理解，希望后续能听到更进阶如 middleware,反爬虫的一些知识点。

# 作业

作业一

- 主要代码: home_work1.py
- csv文件: movie.csv

作业二

- 主要代码: maoyan\maoyan\spiders\maoyan_movie.py
- csv文件: maoyan\movie-spider.csv


# 個人小筆記(未整理凌亂)
## bs4 使用用
###  element find
1. find_all('a',attr={'class':'hd'})
2. find
### element attribute
el.get('href')
## scrapy 
### command
- create project
```bash
# create project test
scrapy startproject test

# create spider for yahoo html
scrapy genspider yahoo www.yahoo.com.tw

# run spider
scrapy crawl yahoo
```
### 架构
spider
- start_requests : spider 第一次发起的请求
- parse function
    - 明确以 yield 返回结果
    - scrapy.Request
        - url
        - meta
        - callback

# 本周作业要求
作业一：
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
# 作业二：
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
猫眼电影网址： https://maoyan.com/films?showType=3
要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。