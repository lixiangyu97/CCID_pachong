import requests
from lxml import html
import json
import time
import pandas as pd
import csv
import xlwt


url = 'http://www.lninfo.gov.cn/cxpt/gcjsyjzx/201804/t20180428_3238072.html'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
html_text = resp.text
selector=html.fromstring(html_text)
print(selector)
tr_list = selector.xpath('/html/body/div/div/div/div[3]/div/div/table/tbody/tr')
print(len(tr_list))
print(tr_list)
for tr in tr_list[1:-1]:
    line=tr.xpath('td/text()')
    list_information.append(line)
print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
dataFrame.to_csv('./辽宁省工程技术研究中心.csv',encoding='gbk')

def csv_to_xlsx_pd():
    csv = pd.read_csv('辽宁省工程技术研究中心.csv', encoding='gbk')
    csv.to_excel('辽宁省工程技术研究中心.xlsx', sheet_name='data')

if __name__ == '__main__':
    csv_to_xlsx_pd()
