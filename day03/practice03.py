#-*- coding:UTF-8 -*-
# str='a\nb'
# str_r=r'a\nb'
# str_zy='a\\nb'
# print('str',str)
# print('str_r',str_r)
# print('str_zy',str_zy)
# print('str',len(str))
# print('str_r',len(str_r))
# print('str_zy',len(str_zy))

'''
<a class="article-item-title weight-bold" href="/p/5194130" target="_blank" rel="noopener noreferrer">最前线 | 字节跳动或很快推出音乐产品，面向海外避开与腾讯音乐正面竞争</a>
<a class="recommend-motif-item-description ellipsis-2" href="/p/5193517" target="_blank" rel="noopener noreferrer">软件是不是真的在蚕食世界？</a>
'''
import re,requests
url = 'http://36kr.com/'
headers_36 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
response = requests.get(url,headers=headers_36)
response.encoding = 'UTF-8'

if response.status_code == 200:
    pattern = re.compile('rel=.+?>([^<]+)</a>')
    text = response.text
    list0 = pattern.findall(text)
    for i in list0:
        print(i)
































