import requests
from lxml import html
import json
import time
import pandas as pd
import csv
import xlwt


url = 'http://dost.hainan.gov.cn/kjfw/kjzy/gcjszx/201609/t20160919_704563.html'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
html_text = resp.text
selector=html.fromstring(html_text)
print(selector)
tr_list = selector.xpath('//*[@id="zoom"]/div/div/div[1]/table/tbody/tr')
print(len(tr_list))
print(tr_list)
for tr in tr_list:
    line=tr.xpath('td/p/span/text()')
    list_information.append(line)
print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
dataFrame.to_csv('./海南省工程技术研究中心.csv',encoding='utf-8')

def csv_to_xlsx_pd():
    csv = pd.read_csv('海南省工程技术研究中心.csv', encoding='utf-8')
    csv.to_excel('海南省工程技术研究中心.xlsx', sheet_name='data')

if __name__ == '__main__':
    csv_to_xlsx_pd()
