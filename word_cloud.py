# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 00:25:10 2017

@author: Yoga Lin
"""

from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

words = open('cloud.txt')
word_count = []
for line in words.readlines():
    word = line.strip().split(':')
    word_count.append((unicode(word[0]), int(word[1])))

bg_mask = np.array(Image.open('timg.png'))

wc = WordCloud( font_path='./font/msyh.ttc',#设置字体
                background_color="white", #背景颜色
                max_words=2000,# 词云显示的最大词数
                mask = bg_mask,
                max_font_size=90, #字体最大值
                random_state=41,
                scale = 3
                )
                
wc.fit_words(word_count)
image_colors = ImageColorGenerator(bg_mask)

plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis('off')
plt.show()
wc.to_file('test.png')