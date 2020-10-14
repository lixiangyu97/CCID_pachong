import requests
from lxml import html
import json
import time
import pandas as pd
import xlwt
url = 'http://kw.beijing.gov.cn/col/col145/index.html?uid=2761&pageNum=1'
from selenium import webdriver
browser=webdriver.Chrome()
browser.get(url)
# print(browser.page_source)
browser.close()
list_information = []
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# html_text = resp.text
# print(html_text)
selector=html.fromstring(browser.page_source)
print(selector)

tr_list = selector.xpath('//*[@id="2761"]/div/div/div[2]/ul/li')
print(len(tr_list))
print(tr_list)
for tr in tr_list[1:-1]:
        line=tr.xpath('span/text()')
        print(line)
        list_information.append(line)


print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
# dataFrame.to_csv('./北京实验室.csv',encoding='gbk')
# def csv_to_xlsx_pd():
#     csv = pd.read_csv('北京实验室.csv', encoding='gbk')
#     csv.to_excel('北京实验室.xlsx', sheet_name='data')
#
# if __name__ == '__main__':
#     csv_to_xlsx_pd()
