# mayday_lyric_analyze
五月天104首歌曲的分词词频统计以及可视化

## 歌词数据爬取

从千千音乐爬取『五月天』的歌词，存入 ```lyric``` 文件夹中

### 启动

```
python spider.py
```

### 介绍

通过构造音乐网站的搜索列表页 [http://music.taihe.com/search/song?s=1&key=五月天&start=20&size=20&third_type=0](http://music.taihe.com/search/song?s=1&key=五月天&start=20&size=20&third_type=0)，翻页获取『五月天』的歌曲链接。

```
# 详细请参考 spider.py 文件

if __name__ == "__main__":
  for page in range(25):
    search_url = lyric_search_template.format('五月天', 20 * page)
    html = get_page(search_url)
    song_urls = parse_search_page(html)

    for song in song_urls:
      song_html = get_page(taihe_host + song['url'])
      lyric_url = get_lyric_url(song_html)
      print('page: %d | name: %s | url: %s' % (page, song['name'], lyric_url))
      download_file(lyric_url, song['name'])
      time.sleep(0.5)
```

## 歌词分词

### 对歌词文件进行简单处理

我们平常听歌时候看到的歌词都是这样的 时间+文字 的lrc格式，但是文件中的广告，如下。会影响到我们对词频统计的判断，故先去除。然后就是歌曲的标题信息等也要去除，只保留时间和歌词文本。（时间可以用正则表达式过滤）

![歌词图片](https://www.z4a.net/images/2019/05/30/113665905bead678823a22a5fd7e4565.jpg)


### 读取各个lrc文件并分词统计词频

使用了 ```from collections import Counter``` 来统计词频，这部分比较简单，参考代码 ```lyric.py```

## 查看初步统计结果

看到统计结果确实统计出了各个词语在不同歌曲出现的次数，但是  的|我|是|你  这种常见停词的出现次数并不是我们关心的重点，换句话说 "什么歌都有这些词好吗!"

![词频统计结果](https://www.z4a.net/images/2019/05/30/4213b5872989b967abe0fa4d8a8b286a.png)

![气泡图](https://www.z4a.net/images/2019/05/30/d2c0bb8e9ed5a97d17fee805de04a675.jpg)

于是我们用一些规则去筛选掉这些停词，比如我们只关心长度大于等于2的词语，频数大于10的词语，然后我们能看到大概想要的结果了。

(基于新数据)

![词频统计结果2](https://www.z4a.net/images/2019/05/30/1559226380981.jpg)

## 简单分析

可以看出

1. 肯定词 是|能 等比其否定形式 不是|不能 出现的次数多
2. 我 比 你 出现的次数多
3. 世界、如果、人生 这种与青春挂钩的词语出现的概率也很高

所以说如果你想写一首 五月天风格的歌曲的话，不妨尝试一下用 世界|人生|回忆|最后|后来|未来|眼泪|梦 这些词语

## 词云生成

```
python word_cloud.py
```

![词云](https://www.z4a.net/images/2019/05/30/7e8475e8faf1aac88274739bfffd1413.jpg)
