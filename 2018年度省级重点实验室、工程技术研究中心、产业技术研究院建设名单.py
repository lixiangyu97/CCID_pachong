import requests
from lxml import html
import json
import time
import pandas as pd
import xlwt


url = 'http://www.ctoutiao.com/434702.html'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
html_text = resp.text
selector=html.fromstring(html_text)
tr_list = selector.xpath('/html/body/div[5]/div[1]/div[1]/div[2]/div[2]/table[3]/tbody/tr')
print(len(tr_list))
print(tr_list)
for tr in tr_list[:]:
        line=tr.xpath('td/p/span/text()')
        print(line)
        list_information.append(line)

print(list_information)
dataFrame = pd.DataFrame(list_information)
print(dataFrame)
dataFrame.to_csv('./3.csv',encoding='gbk')



# book = xlwt.Workbook()
# sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
#
# i = 1
# for list in line:
#         j = 0
#         for data in list:
#                 sheet1.write(i, j, data)
#                 j += 1
#         i += 1
#         book.save('国家重点研发计划“智能机器人”重点专项拟立项的2018年度项目公示清单.xls')


