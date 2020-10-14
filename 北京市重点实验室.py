import requests
from lxml import html
import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib import request
import xlwt
# 获取数据
value = 1
while value <= 16:
    value0 = str(value)
    url = "http://kw.beijing.gov.cn/col/col145/index.html?uid=2761&pageNum=" + value0 + ".htm"
    # url="http://www.hs-bianma.com/hs_chapter_01.htm"
    # '''此行可以自行更换代码用来汇集数据'''
    response = request.urlopen(url)
    html = response.read()
    html = html.decode("utf-8")
    bs = BeautifulSoup(html, 'lxml')

    # 内容处理
    content = bs.find_all('span')
    print(content)
    data_list_content = []
    for data in content:
        data_list_content.append(data.text.strip())
        print()
    new_list = [data_list_content[i:i + 2] for i in range(0, len(data_list_content),2)]
    print(new_list)
    # 存入excel表格
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)

    # 标题存入
    # heads = data_list_title[:]
    # ii = 0
    # for head in heads:
    #     sheet1.write(0, ii, head)
    #     ii += 1
        # print(head)

    # 内容录入
    i = 1
    for list in new_list:
        j = 0
        for data in list:
            sheet1.write(i, j, data)
            j += 1
        i += 1

    # 文件保存
    # book.save('sum' + value0 + '.xls')
    value += 1
    print(value0 + "写入完成！")
print("全部完成")



# url = 'http://kw.beijing.gov.cn/col/col145/index.html?uid=2761&pageNum=1'
# list_information = []
# resp = requests.get(url)
# resp.encoding = 'utf-8'
# html_text = resp.text
# selector=html.fromstring(html_text)
# tr_list = selector.xpath('//*[@id="js_content"]/section[2]/table/tbody/tr')
# print(len(tr_list))
# print(tr_list)
# for tr in tr_list[1:-1]:
#         line=tr.xpath('td/text()')
#         print(line)
#         list_information.append(line)
# print(list_information)
# dataFrame = pd.DataFrame(list_information)
# print(dataFrame)
# dataFrame.to_csv('./国家重点研发计划“智能机器人”重点专项拟立项的2018年度项目公示清单.csv',encoding='gbk')





