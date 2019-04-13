#-*- coding:UTF-8 -*-

'''
//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a
//*[@id="thread_list"]/li[3]/div/div[2]/div[1]/div[1]/a
//*[@id="thread_list"]/li[5]/div/div[2]/div[1]/div[1]/a
//*[@id="thread_list"]/li[4]/div/div[2]/div[1]/div/a

'''

from selenium import webdriver
import time
# browser = webdriver.Chrome('../bin/chromedriver.exe')
# url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%95%B0%E5%AD%A6&red_tag=b1441715300'
# browser.get(url)
# #窗口最大化
# browser.maximize_window()
# #睡眠等待页面加载
# time.sleep(2)
# #查找多个标签，返回一个列表
# list0 = browser.find_elements_by_xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a')
# #输出列表对象的文本
# for i in list0:
#     try:
#         print(i.text)
#     except:
#         pass
# #退出浏览器
# browser.quit()

#>>>>>>>>>>>>>>>>>>>>>>>方法2<<<<<<<<<<<<<<<<<<<<<<<<<<

# browser = webdriver.Chrome()
# url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%95%B0%E5%AD%A6&red_tag=b1441715300'
# browser.get(url)
# #窗口最大化
# browser.maximize_window()
# #睡眠等待页面加载
# time.sleep(2)
# #查找多个标签，返回一个列表
# list0 = browser.find_elements_by_xpath('//*[@id="thread_list"]/li[position()<last()+1]/div/div[2]/div[1]/div[1]/a')
# #输出列表对象的文本
# for i in list0:
#     print(i.text)
# #退出浏览器
# browser.quit()

#>>>>>>>>>>>>>>>>>>>>>>>方法3<<<<<<<<<<<<<<<<<<<<<<<<<<

url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%95%B0%E5%AD%A6&red_tag=b1441715300'
num = 1
browser = webdriver.Chrome()
def printTitle(url):
    global num
    global browser
    browser.get(url)
    # 窗口最大化
    browser.maximize_window()
    # 睡眠等待页面加载
    time.sleep(2)
    # 查找多个标签，返回一个列表
    list0 = browser.find_elements_by_xpath('//*[@id="thread_list"]/li')
    print('>'*45,'第%d页'%num,'<'*45)
    # 输出列表对象的文本
    for element in list0:
        try:
            print(element.find_element_by_xpath('./div/div[2]/div[1]/div[1]/a').text)
            print(element.find_element_by_xpath('./div/div[2]/div[1]/div[1]/a').get_attribute('href'))
        except:
            pass
    #找到下一页，递归
    url = browser.find_element_by_xpath('//*[@id="frs_list_pager"]/a').get_attribute('href')
    num += 1
    if num < 4:
        printTitle(url)
    else:
        # 退出浏览器
        browser.quit()

printTitle(url)

# //*[@id="frs_list_pager"]/a[10]
#//*[@id="frs_list_pager"]/a[12]










