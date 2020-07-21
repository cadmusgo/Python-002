# 学习笔记

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

### 架構
spider
- start_requests : spider 第一次發起的請求
- parse function
    - 明確以 yield 返回結果
    - scrapy.Request
        - url
        - meta
        - callback



## 學習心得

## TODO
1. 明確識別、區分 download、spider middleware。



## QA


## 本周作業
### 作业一：
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。


### 作业二：
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

猫眼电影网址： https://maoyan.com/films?showType=3

要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。