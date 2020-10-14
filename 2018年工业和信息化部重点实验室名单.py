import requests
from lxml import html
import json
import time
import pandas as pd
import xlwt


url = 'https://http://www.most.gov.cn/mostinfo/xinxifenlei/fgzc/gfxwj/gfxwj2018/201806/t20180604_139746.htm'
list_information = []
resp = requests.get(url)
resp.encoding = 'utf-8'
html_text = resp.text
selector = html.fromstring(html_text)
tr_list = selector.xpath('//*[@id="Zoom"]/table[1]/tbody/tr')
print(len(tr_list))
del tr_list[1]
del tr_list[12]
del tr_list[41]
for tr in tr_list:
        line=tr.xpath('td/p/span[1]/text()')
        print(line)
        list_information.append([line[0],line[1],line[2],line[3]])

print(list_information)
# book = xlwt.Workbook()
#
# sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
#
# i = 1
# for list in list_information:
#         j = 0
#         for data in list:
#                 sheet1.write(i, j, data)
#                 j += 1
#         i += 1
#         book.save('国家重点研发计划“智能机器人”重点专项拟立项的2018年度项目公示清单.xls')
# dataFrame = pd.DataFrame(data=list_information)
# print(dataFrame)
# dataFrame.to_excel('./2018年工程领域和材料领域国家重点实验室评估结果.csv',encoding='gbk')



