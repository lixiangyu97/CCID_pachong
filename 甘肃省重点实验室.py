import requests
from lxml import html
import json
import time
import pandas as pd
import csv
import xlwt


url = 'http://kjt.gansu.gov.cn/News_Notice/detail.php?n_no=363197'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
html_text = resp.text
selector=html.fromstring(html_text)
print(selector)
tr_list = selector.xpath('//*[@id="newbody"]/font/table/tbody/tr')  #//*[@id="newbody"]/font/table/tbody/tr[1]/td[1]/p/b/span
print(len(tr_list))
print(tr_list)
for tr in tr_list[1:-1]:
    line=tr.xpath('td/p/b/span/text()')
    list_information.append(line)
print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
dataFrame.to_csv('./甘肃省重点实验室.csv',encoding='gbk')

def csv_to_xlsx_pd():
    csv = pd.read_csv('甘肃省重点实验室.csv', encoding='gbk')
    csv.to_excel('甘肃省重点实验室.xlsx', sheet_name='data')

if __name__ == '__main__':
    csv_to_xlsx_pd()


