"""
作業要求:
    1. 安装并使用 requests、bs4 库
    2. 爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间
    3. UTF-8 字符集保存到 csv 格式的文件中。

開發說明:
"""
__authoer__ = 'cadmus'

import requests
from bs4 import BeautifulSoup

# parse html
def parse(html):
    soup = BeautifulSoup(html, 'html.parser')

    movie_list = []
    for div in soup.find_all('div', attrs={'class': 'movie-item-hover'}):
        div_list = div.find_all('div', {'class': 'movie-hover-title'})

        title = div_list[0].find('span').text.strip()
        movie_type = stripText(div_list[1].text)
        movie_time = stripText(div_list[3].text)

        movie_list.append(dict(
            title=title,
            movie_type=movie_type,
            movie_time=movie_time
        ))

    return movie_list

# get maoyan html
def get_html():
    html = ''
    if IS_TEST_MODE:
        with open('sample.html', 'r', encoding='utf-8') as f:
            html = f.read()
    else:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
        url = 'https://maoyan.com/films?showType=3'
        response = requests.get(url, headers={'user-agent': user_agent})
        html = response.text

    return html


def save_to_csv(movie_list):
    with open('./movie.csv','w',encoding='utf-8') as f:
        for movie in movie_list:
            print(f'{movie["title"]},{movie["movie_type"]},{movie["movie_time"]}')
            f.write(f'{movie["title"]},{movie["movie_type"]},{movie["movie_time"]}\n')

def stripText(text):
    return text.strip().replace('类型:', '').replace(' ', '').replace('\n', ' ').replace('\r', '')

# 是否為本地測試
IS_TEST_MODE = True
if __name__ == "__main__":
    html = get_html()
    movie_list = parse(html)
    save_to_csv(movie_list)



