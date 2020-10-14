import requests
from lxml import html
import json
import time
import pandas as pd
import csv
import xlwt


url = 'http://www.gxst.gov.cn/gxkjt/xxgk/20181204/002016004_ac7c1d00-f249-4123-a06c-092ecea439a0.htm'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)
html_text = resp.text
selector=html.fromstring(html_text)
print(selector)
tr_list = selector.xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr')  #/html/body/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/p/b/span
print(len(tr_list))
print(tr_list)
for tr in tr_list:
    line=tr.xpath('td/p/span/text()')
    list_information.append(line)
print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
dataFrame.to_csv('./广西重点实验室.csv',encoding='utf-8',index=0)

def csv_to_xlsx_pd():
    csv = pd.read_csv('广西重点实验室.csv', encoding='utf-8')
    csv.to_excel('广西重点实验室.xlsx', sheet_name='data')

if __name__ == '__main__':
    csv_to_xlsx_pd()
