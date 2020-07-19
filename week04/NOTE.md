# Pandas常用命令集

```python
import pandas as pd
import os

# 获取文件小技巧
pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd, 'book_utf8.csv')

# DataFrame type
df = pd.read_csv(book)  # read_csv(path)

# 筛选特定的列显示
df[column_name]

# slicing针对的是行
# loc(slicing, [column_name])则是筛选特定的行、列
df.loc(1:3, ['star'])

# 数据聚合
# groupby(column_name), 分组结束后要进行汇总
# 因为groupby返回的是 DataFrameGroupBy object
df.groupby('star').sum()

# 映射创建新列
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)
```



# Pandas的基本数据类型



## Series

```python
# creation
# pd.Series(list,dict)
# pd.Series(list, index = list)

# attributes, methods
# Series.index; Series.values
# Series.values.tolist()
# Series.map(func_object)
```



## Data Frame

```python
# creation
# pd.DataFrame(list, dict)
# pd.DataFrame(nested_list)

# attributes
# DataFrame.columns
# DataFrame.index
```



# jieba中文分词



## 支持分词的模式

- 精确模式：适合文本分析
- 全模式： 所有成词的词语都扫描，但不能解决歧义
- 搜索引擎模式： 基于精确模式，并对长词进行再切分
- paddle模式： 利用PaddlePaddle深度学习框架， 需要安装paddlepaddle-tiny包



## 主要功能介绍

1. 分词

- jieba.cut(string, cut_all = False, HMM = True, use_paddle = False)

if cut_all = True: 采用全模式 else: 采用精确模式

- jieba.cut_for_search(string, HMM = True)

以上两种方法返回的结果都是生成器，接下来的两种方法类似上面，不过返回的是列表类型

- jiaba.lcut(string, cut_all, HMM, use_paddle)
- jieba.lcut_for_search(string, HMM)

2. 添加自定义词典

采用的是 jieba.load_userdict(file_name).

自定义的词典的内容格式： 词语 词频(可省略) 词性(可省略)

以上的添加方式是静态的，如果想动态地添加和删除词的话，可以采用 add_word(word, freq = None, tag = None) 和 del_word(word); 还可以动态调节词频: suggest_freq(segment, tune = True)

```python
>>> print('/'.join(jieba.cut('如果放到post中将出错。', HMM = False)))
如果/放到/post/中将/出错/。
>>> jieba.suggest_freq(('中','将'))
>>> print('/'.join(jieba.cut('如果放到post中将出错。', HMM = False)))
如果/放到/post/中/将/出错/。
```

3. 关键词提取

- 基于 TF-IDF算法

jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())

@topK:  返回几个权重最大的关键词

@withWeight: 是否连同权重值一起返回

@allowPOS: 仅包括指定词性的词



jieba.analyse.set_stop_words(file_name)

自定义语料内容的格式： 每行一个词

- 基于TextRank算法

jiaba.analyse.textrank(sentence, topK = 20, withWeight = False, allowPOS = ('ns', 'n', 'vn', 'v'))

4. 词性标注

```python
import jieba
import jieba.posseg as pseg

>>> words = jieba.cut("我爱北京天安门")
>>> print(list(words))
['我', '爱', '北京', '天安门']
>>> result = pseg.cut("我爱北京天安门")
>>> print(list(result))
[pair('我', 'r'), pair('爱', 'v'), pair('北京', 'ns'), pair('天安门', 'ns')]
# posseg分词结果会带词性内容
```

| 标签 | 含义     | 标签 | 含义     | 标签 | 含义     | 标签 | 含义     |
| ---- | -------- | ---- | -------- | ---- | -------- | ---- | -------- |
| n    | 普通名词 | f    | 方位名词 | s    | 处所名词 | t    | 时间     |
| nr   | 人名     | ns   | 地名     | nt   | 机构名   | nw   | 作品名   |
| nz   | 其他专名 | v    | 普通动词 | vd   | 动副词   | vn   | 名动词   |
| a    | 形容词   | ad   | 副形词   | an   | 名形词   | d    | 副词     |
| m    | 数量词   | q    | 量词     | r    | 代词     | p    | 介词     |
| c    | 连词     | u    | 助词     | xc   | 其他虚词 | w    | 标点符号 |
| PER  | 人名     | LOC  | 地名     | ORG  | 机构名   | TIME | 时间     |

5. 并行分词

针对的是多行文本的情形，其实就是开启Python的多进程。 目前不支持Windows

开启并行分词模式： jieba.enable_parallel(number_of_processes)

关闭并行分词模式： jieba.disable_parallel()

