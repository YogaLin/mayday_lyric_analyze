# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:01:23 2019

@author: Yoga Lin
"""

import requests
from lxml import etree
import time

taihe_host = 'http://music.taihe.com'
lyric_search_template = 'http://music.taihe.com/search/song?key={}&start={}&size=20'

# 获取页面 html 文档
def get_page(url, encoding='utf-8'):
  try:
    r = requests.get(url)
    r.encoding = encoding
    return r.text
  except Exception, e:
    print('Error:', url, e)

# 下载歌词文件
def download_file(url, name):
  try:
    r = requests.get(url)
    with open('./lyric/%s.lrc' % name, 'wb') as fw:
      fw.write(r.content)
  except Exception, e:
    print('Error:', url, name, e)

# 解析搜索页面
# 返回歌词链接列表
def parse_search_page(html):
  urls = []
  tree = etree.HTML(html)
  data = tree.xpath('//*[@id="result_container"]/div[1]/div[1]/ul/li')
  for i in data:
    link = i.xpath('div[1]/span[4]/a[1]/@href')
    song_name = i.xpath('div[1]/span[4]/a[1]/text()')
    if len(link) > 0 and len(song_name) > 0:
      urls.append({
        'url': link[0],
        'name': song_name[0]
      })
  return urls

# 获取歌曲页面的歌词下载链接
def get_lyric_url(html):
  tree = etree.HTML(html)
  lyric_url = tree.xpath('//*[@id="lyricCont"]/@data-lrclink')
  return lyric_url[0] if len(lyric_url) > 0 else None

if __name__ == "__main__":
  for page in range(25):
    search_url = lyric_search_template.format('五月天', 20 * page)
    html = get_page(search_url)
    song_urls = parse_search_page(html)
    # print(song_urls)
    for song in song_urls:
      song_html = get_page(taihe_host + song['url'])
      lyric_url = get_lyric_url(song_html)
      print('page: %d | name: %s | url: %s' % (page, song['name'], lyric_url))
      download_file(lyric_url, song['name'])
      time.sleep(0.5)
      # break

    # break
