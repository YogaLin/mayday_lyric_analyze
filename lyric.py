# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 22:54:14 2017

@author: Yoga Lin
"""

import os, sys
import re
import jieba
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf8')

all_words = [] # 保存各个词在不同歌曲出现的次数
# 依次读取歌词文件
for file_name in os.listdir('lyric'):
    with open('lyric/' + file_name) as lrc:
        words = re.sub(r'\[.+\]', '', lrc.read()) # 正则匹配歌词内容
        cut_words = jieba.cut(words) # Jieba中文分词，将一句歌词切割成多个词语
        all_words.extend(set(cut_words)) # 将分词结果用set过滤，同一个词语在同一首歌内仅统计一次

count = Counter(all_words) # 计算次数
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True) # 排序统计结果

# 保存结果
fw = open('more_than_two_words.txt', 'wb')
for item in sorted_count:
    if len(item[0])>1:
        fw.write(item[0] + ':' + str(item[1]) + '\n')
fw.close()
'''
fw = open('result.txt', 'wb')
for item in sorted_count:
    #print item[0] + ':' + item[1] + '\n'
    fw.write(item[0] + ':' + str(item[1]) + '\n')
fw.close()
'''