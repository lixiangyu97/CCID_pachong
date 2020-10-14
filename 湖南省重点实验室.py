import requests
from lxml import html
import json
import time
import pandas as pd
import csv
import xlwt


url = 'http://kjt.hunan.gov.cn/zxgz/cxpt/szsys/201605/t20160517_3058454.html'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)
html_text = resp.text
selector=html.fromstring(html_text)
print(selector)
tr_list = selector.xpath('//*[@id="j-show-body"]/div/div/table/tbody/tr')
print(len(tr_list))
print(tr_list)
for tr in tr_list:
    line=tr.xpath('td/text()')
    list_information.append(line)
print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
# dataFrame.to_csv('./湖南省工程技术研究中心.csv',encoding='utf-8',index=0)
dataFrame.to_excel('湖南省工程技术研究中心.xlsx', sheet_name='data',index=0)
# def csv_to_xlsx_pd():
#     csv = pd.read_csv('湖南省工程技术研究中心.csv', encoding='utf-8')
#     csv.to_excel('湖南省工程技术研究中心.xlsx', sheet_name='data')

# # if __name__ == '__main__':
#     csv_to_xlsx_pd()
